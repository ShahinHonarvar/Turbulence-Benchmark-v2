from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    sorted_str_list = sorted(str_list, key=len)
    for str1, str2 in combinations(sorted_str_list, 2):
        if len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2)):
            count = 0
            for s in sorted_str_list:
                if sorted(s) == sorted(str1):
                    count += 1
            if count >= 209:
                return True
    return False