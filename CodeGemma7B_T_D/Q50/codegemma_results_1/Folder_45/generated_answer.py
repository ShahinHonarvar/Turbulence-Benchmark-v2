from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            str_dict[tuple(sorted(s.lower()))].append(s)
    result = 0
    for anagrams in str_dict.values():
        result += len(anagrams) * (len(anagrams) - 1) // 2
    return result >= 277