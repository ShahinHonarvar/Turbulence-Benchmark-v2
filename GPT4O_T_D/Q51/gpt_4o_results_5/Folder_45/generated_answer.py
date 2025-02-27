from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for s1, s2 in combinations(normalized_strings, 2):
        if s1 == s2:
            count += 1
        if count > 464:
            return False
    return True