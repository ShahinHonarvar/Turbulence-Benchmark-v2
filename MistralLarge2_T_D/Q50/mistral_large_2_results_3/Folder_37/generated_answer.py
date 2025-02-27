from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(key) >= 3 and len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs >= 29