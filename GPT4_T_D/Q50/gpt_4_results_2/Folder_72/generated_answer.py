from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            freq[''.join(sorted(s.lower()))].append(s)
    count = sum((len(values) * (len(values) - 1) // 2 for values in freq.values() if len(values) > 1))
    return count >= 55