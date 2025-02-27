from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagrams[sorted_str].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return count >= 43