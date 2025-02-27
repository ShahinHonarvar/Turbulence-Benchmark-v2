import itertools

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(lst):
    anagrams = [list(group) for key, group in itertools.groupby(sorted(lst, key=sorted), key=sorted) if len(group) > 1]
    return sum((len(group) <= 54 for group in anagrams if len(group[0]) >= 3)) <= len(anagrams)