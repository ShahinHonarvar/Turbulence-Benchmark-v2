from collections import Counter

def if_contains_anagrams(strs):
    count = 0
    pairs = {}
    for s in strs:
        if len(s) >= 3:
            s = s.lower()
            counter = Counter(s)
            key = ''.join(sorted(s))
            if key in pairs:
                pairs[key] += 1
            else:
                pairs[key] = 1
    pair_counts = list(pairs.values())
    pair_counts.sort()
    for i in range(len(pair_counts) - 1, 0, -1):
        count += pair_counts[i]
    return count <= 84