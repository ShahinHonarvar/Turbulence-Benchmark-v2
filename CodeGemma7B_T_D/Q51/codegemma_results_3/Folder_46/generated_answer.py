from collections import defaultdict

def if_contains_anagrams(str_list):
    num_anagrams = 0
    str_map = defaultdict(list)
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        if len(s) < 3:
            continue
        str_map[s].append(s)
    for group in str_map.values():
        num_anagrams += len(group) * (len(group) - 1) // 2
    return num_anagrams <= 61