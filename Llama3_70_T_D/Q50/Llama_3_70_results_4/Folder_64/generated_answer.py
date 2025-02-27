from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.casefold()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 5