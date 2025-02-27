from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    count = 0
    for group in anagrams.values():
        n = len(group)
        if n >= 2:
            count += n * (n - 1) // 2
    return count >= 49