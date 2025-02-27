from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams.values() if v > 1))
    return pairs >= 98