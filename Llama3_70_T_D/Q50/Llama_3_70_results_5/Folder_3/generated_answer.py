from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    pairs = 0
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(sorted(s.lower()))
        count[s] += 1
        pairs += count[s] - 1
    return pairs >= 30