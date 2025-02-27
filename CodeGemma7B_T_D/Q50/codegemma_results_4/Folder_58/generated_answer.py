from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        str_dict[''.join(sorted(s.lower()))].append(s)
    count = 0
    for v in str_dict.values():
        if len(v) >= 3:
            count += len(v) * (len(v) - 1) // 2
    result = count >= 411
    return result