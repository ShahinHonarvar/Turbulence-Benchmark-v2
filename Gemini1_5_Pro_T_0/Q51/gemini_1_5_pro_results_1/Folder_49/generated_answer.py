from itertools import combinations

def if_contains_anagrams(list_of_strings):
    count = 0
    for str1, str2 in combinations(list_of_strings, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1.lower()) == sorted(str2.lower())):
            count += 1
    return count <= 10