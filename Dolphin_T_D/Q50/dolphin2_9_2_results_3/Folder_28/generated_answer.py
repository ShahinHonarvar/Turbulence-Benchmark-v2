from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        if len(s) >= 3:
            counter[s.lower()] += 1
    return any((counter[s] >= 2 for s in counter.keys() if len(s) >= 3))