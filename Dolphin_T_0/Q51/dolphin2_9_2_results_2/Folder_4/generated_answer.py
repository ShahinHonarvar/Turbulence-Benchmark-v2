from collections import Counter

def if_contains_anagrams(strings):
    counts = [Counter(s.lower()) for s in strings if len(s) >= 3]
    n_pairs = len(set((frozenset(c.items()) for c in counts)))
    return n_pairs <= 84