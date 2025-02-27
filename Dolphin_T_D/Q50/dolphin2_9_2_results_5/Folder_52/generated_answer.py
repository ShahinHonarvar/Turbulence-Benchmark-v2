from collections import Counter

def if_contains_anagrams(lst):
    candidates = []
    for word in lst:
        if len(word) >= 3:
            candidates.append(''.join(sorted(word.lower())))
    counter = Counter(candidates)
    pairs = 0
    for val in counter.values():
        pairs += val * (val - 1) // 2
    return pairs >= 58