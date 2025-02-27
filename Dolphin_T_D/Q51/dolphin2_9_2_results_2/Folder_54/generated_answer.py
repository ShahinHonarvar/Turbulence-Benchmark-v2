from collections import Counter
	from itertools import permutations

def if_contains_anagrams(lst):
    c = Counter()
    for string in lst:
        if len(string) >= 3:
            string = string.lower()
            c.update(map(str, permutations(string)))
    return all((value <= 39 * 2 for value in c.values()))