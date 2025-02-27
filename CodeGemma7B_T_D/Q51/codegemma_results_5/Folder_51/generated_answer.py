import collections

def if_contains_anagrams(str_list):
    str_map = collections.defaultdict(list)
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        str_map[string].append(string)
    count = 0
    for k, group in str_map.items():
        if len(group) > 1 and len(k) >= 3:
            count += len(group)
    return count <= 116