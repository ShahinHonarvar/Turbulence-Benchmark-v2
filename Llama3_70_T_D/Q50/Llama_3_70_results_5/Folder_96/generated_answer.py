from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            anagrams[sorted_str].append(s)
    count = 0
    for k in anagrams:
        n = len(anagrams[k])
        count += n * (n - 1) // 2
    return count >= 98