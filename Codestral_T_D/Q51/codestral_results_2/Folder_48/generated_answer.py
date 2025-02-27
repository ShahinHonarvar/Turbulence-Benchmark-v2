from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            key = ''.join(sorted(lower_s))
            anagrams[key] = anagrams.get(key, 0) + 1
    return sum((v * (v - 1) // 2 for v in anagrams.values())) <= 277