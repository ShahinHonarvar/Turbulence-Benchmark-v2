from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)
    anagram_pairs_count = sum((1 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs_count <= 30