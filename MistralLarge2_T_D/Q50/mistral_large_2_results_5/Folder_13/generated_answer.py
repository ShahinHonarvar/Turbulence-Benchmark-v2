from itertools import combinations

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(lst):
    count = 0
    for str1, str2 in combinations(lst, 2):
        if len(str1) >= 3 and len(str2) >= 3 and are_anagrams(str1, str2):
            count += 1
        if count >= 144:
            return True
    return False