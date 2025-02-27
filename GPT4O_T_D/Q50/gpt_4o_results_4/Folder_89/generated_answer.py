from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagrams_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams_dict[sorted_str] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagrams_dict.values() if v > 1))
    return anagram_pairs >= 36