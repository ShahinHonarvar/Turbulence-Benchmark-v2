import itertools

def are_anagrams(a, b):
    return sorted(a.lower()) == sorted(b.lower())

def count_anagrams(strings):
    anagrams = [list(group) for key, group in itertools.groupby(sorted(strings, key=sorted), key=sorted) if len(group) > 1]
    return sum((len(group) // 2 for group in anagrams))

def if_contains_anagrams(strings):
    if len(strings) < 2:
        return False
    return count_anagrams(strings) <= 392