from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        key = frozenset(Counter(s).items())
        if key in anagram_dict:
            anagram_dict[key] += 1
        else:
            anagram_dict[key] = 1
    count = 0
    for val in anagram_dict.values():
        count += val * (val - 1) // 2
    return count <= 47