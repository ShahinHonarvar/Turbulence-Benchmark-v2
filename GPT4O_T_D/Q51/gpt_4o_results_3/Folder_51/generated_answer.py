from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            anagram_dict[normalized] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values() if count > 1))
    return pairs_count <= 116