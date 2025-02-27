from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3 and s.isalpha() and s.isascii():
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs <= 66