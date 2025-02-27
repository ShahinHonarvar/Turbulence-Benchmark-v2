from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str] += 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return count <= 61