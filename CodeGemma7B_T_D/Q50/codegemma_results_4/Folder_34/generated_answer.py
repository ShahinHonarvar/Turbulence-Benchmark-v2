from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(int)
    for string in str_list:
        if len(string) >= 3:
            str_map[''.join(sorted(string.lower()))] += 1
    if sum((value ** 2 >= 25 for value in str_map.values())) >= 25:
        return True
    else:
        return False