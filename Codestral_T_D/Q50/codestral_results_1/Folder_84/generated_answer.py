from collections import Counter

def if_contains_anagrams(strings):
    counter = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            counter[sorted_s] = counter.get(sorted_s, 0) + 1
    return any((v >= 2 for v in counter.values()))