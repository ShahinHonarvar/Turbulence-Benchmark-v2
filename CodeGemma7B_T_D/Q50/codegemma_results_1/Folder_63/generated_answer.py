from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            str_dict[key].append(s)
    count = 0
    for val in str_dict.values():
        if len(val) >= 2:
            count += len(val) * (len(val) - 1) // 2
    return count >= 89