from collections import defaultdict

def if_contains_anagrams(strs):
    anagrams = defaultdict(int)
    for s in strs:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return count <= 181