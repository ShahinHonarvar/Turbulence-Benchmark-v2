from collections import defaultdict

def if_contains_anagrams(strs):
    count = 0
    anagrams = defaultdict(list)
    for s in strs:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            anagrams[s].append(s)
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count <= 11