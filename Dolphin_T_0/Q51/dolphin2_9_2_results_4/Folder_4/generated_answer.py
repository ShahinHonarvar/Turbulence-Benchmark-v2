import collections
import itertools

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst]
    lst = [s for s in lst if len(s) >= 3]
    count = 0
    for pair in itertools.combinations(lst, 2):
        if collections.Counter(pair[0]) == collections.Counter(pair[1]):
            count += 1
    return count <= 84