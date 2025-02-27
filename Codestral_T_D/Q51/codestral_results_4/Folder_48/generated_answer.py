from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter((''.join(sorted(s.lower())) for s in lst if len(s) >= 3))
    return sum((x * (x - 1) // 2 for x in counter.values())) <= 277