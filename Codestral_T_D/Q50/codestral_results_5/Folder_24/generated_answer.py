from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
    count = 0
    for lst in d.values():
        n = len(lst)
        count += n * (n - 1) // 2
    return count >= 65