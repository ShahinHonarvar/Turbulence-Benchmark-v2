from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagram_count[normalized] += 1
    num_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return num_pairs <= 173