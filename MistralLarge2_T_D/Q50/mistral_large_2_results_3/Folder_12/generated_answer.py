from collections import defaultdict

def if_contains_anagrams(strings):

    def normalized_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for string in strings:
        if len(string) < 3:
            continue
        normalized = normalized_string(string)
        anagram_count[normalized] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count >= 69