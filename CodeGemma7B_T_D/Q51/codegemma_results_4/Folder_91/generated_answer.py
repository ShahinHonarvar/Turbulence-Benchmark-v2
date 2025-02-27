from itertools import combinations
from collections import defaultdict

def permutations(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    perms = []
    for c in s:
        suffixes = permutations(s[:s.index(c)] + s[s.index(c) + 1:])
        for suffix in suffixes:
            perms.append(c + suffix)
    return perms

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        str_dict[tuple(sorted(s.lower()))].append(s)
    count = 0
    for anagrams in str_dict.values():
        if len(anagrams) > 1:
            count += combinations(anagrams, 2)
    return count <= 88