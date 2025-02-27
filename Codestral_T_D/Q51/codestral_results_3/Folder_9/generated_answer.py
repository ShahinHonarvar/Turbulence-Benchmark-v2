from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter([''.join(sorted(s.lower())) for s in strings if len(s) >= 3])
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 475