from itertools import combinations

def if_contains_anagrams(list_of_strings):
    count = 0
    for i, j in combinations(list_of_strings, 2):
        if len(i) >= 3 and len(j) >= 3 and (sorted(i.lower()) == sorted(j.lower())):
            count += 1
    if count >= 24:
        return True
    else:
        return False