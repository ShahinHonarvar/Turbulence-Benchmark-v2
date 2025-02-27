from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    sorted_str = sorted(str_list, key=sorted)
    count = 0
    for a, b in combinations(sorted_str, 2):
        if len(a) >= 3 and len(b) >= 3 and (sorted(a) == sorted(b)):
            count += 1
    return count >= 18