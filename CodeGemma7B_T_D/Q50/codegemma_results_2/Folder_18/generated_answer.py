from collections import defaultdict

def if_contains_anagrams(str_list):
    str_map = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            str_map[''.join(sorted(s.lower()))].append(s)
    return len(str_map) >= 106