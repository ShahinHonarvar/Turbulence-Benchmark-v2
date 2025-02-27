from collections import defaultdict

def if_contains_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = 0
    for v in anagrams.values():
        count += len(v) * (len(v) - 1) // 2
    return count >= 178