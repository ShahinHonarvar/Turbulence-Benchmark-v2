from collections import Counter

def if_contains_anagrams(lst):
    wrds = {w.lower(): 1 for w in lst if len(w) >= 3}
    anagrams = {k: v for k, v in wrds.items() if len(k) >= 3}
    pairs = 0
    for k, v in anagrams.items():
        pairs += sum((1 for key, value in anagrams.items() if Counter(key) == Counter(k) and key != k))
    return pairs >= 178