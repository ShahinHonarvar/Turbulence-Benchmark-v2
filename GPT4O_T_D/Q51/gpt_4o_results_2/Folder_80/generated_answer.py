from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(string):
        return ''.join(sorted(string.lower()))
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagram_groups[normalized] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return pairs_count <= 255