import itertools

def are_anagrams(a, b):
    return sorted(a.lower()) == sorted(b.lower())

def if_contains_anagrams(strings):
    anagrams = [list(group) for key, group in itertools.groupby(sorted(strings, key=sorted), key=sorted) if len(group) >= 3]
    return len(anagrams) >= 189