import itertools

def if_contains_anagrams(lst):
    perms = [''.join(p) for p in itertools.permutations('abcdefghijklmnopqrstuvwxyz')]
    ans = 0
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 and len(word1) >= 3 and (len(word2) >= 3) and (sum((a == b for a, b in zip(sorted(word1.lower()), sorted(word2.lower())))) >= len(word1) - 1):
                ans += 1
    if ans > 445:
        return False
    return True