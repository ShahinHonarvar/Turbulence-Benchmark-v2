import itertools

def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

def if_contains_anagrams(strings):
    anagrams = [list(group) for key, group in itertools.groupby(sorted(strings, key=sorted), key=sorted) if len(group) >= 3]
    return sum((len(group) * (len(group) - 1) // 2 for group in anagrams)) >= 68