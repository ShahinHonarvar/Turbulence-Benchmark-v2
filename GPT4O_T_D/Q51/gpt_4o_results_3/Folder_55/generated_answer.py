from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize_string(s)
            anagram_count[normalized] += 1
    pairs_count = 0
    for count in anagram_count.values():
        if count > 1:
            pairs_count += count * (count - 1) // 2
    return pairs_count <= 44