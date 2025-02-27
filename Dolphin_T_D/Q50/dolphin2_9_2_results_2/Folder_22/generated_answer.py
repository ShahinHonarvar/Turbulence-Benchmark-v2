from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count_set = set()
    for comb in combinations(lst, 2):
        str1, str2 = comb
        if len(str1) < 3 or len(str2) < 3:
            continue
        sorted_str1 = sorted(str1.lower())
        sorted_str2 = sorted(str2.lower())
        if sorted_str1 == sorted_str2:
            count_set.add((str1, str2))
            count_set.add((str2, str1))
    return len(count_set) >= 72