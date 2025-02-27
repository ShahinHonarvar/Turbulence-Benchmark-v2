from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if s.isalpha() and len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 52