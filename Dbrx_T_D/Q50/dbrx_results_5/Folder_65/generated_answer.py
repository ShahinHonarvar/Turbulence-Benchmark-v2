import itertools

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(strings):
    anagrams = [list(group) for key, group in itertools.groupby(sorted(strings, key=sorted), key=sorted) if len(group) >= 3]
    return len(list(itertools.combinations(anagrams, 2))) >= 94