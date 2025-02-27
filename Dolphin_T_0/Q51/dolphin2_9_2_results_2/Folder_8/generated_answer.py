from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    anagrams = set()
    for perm in permutations(map(ord, 'a' * 3)):
        anagrams.add(''.join(map(chr, perm)))
    for s1, s2 in zip(lst, lst[1:]):
        low1, low2 = map(str.lower, s1, s2)
        if len(low1) < 3 or len(low2) < 3:
            return False
        if sorted(low1) in anagrams and sorted(low2) in anagrams:
            Counter(low1) == Counter(low2)
            return False
    return True