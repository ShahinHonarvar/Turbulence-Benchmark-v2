from collections import defaultdict

def if_contains_anagrams(strings):
    d = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            d[key].append(s)
    count = 0
    for anagrams in d.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 14