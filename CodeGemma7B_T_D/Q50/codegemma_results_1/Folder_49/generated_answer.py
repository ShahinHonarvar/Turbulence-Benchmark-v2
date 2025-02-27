from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        str_dict[key].append(s)
    count = 0
    for k in str_dict.values():
        n = len(k)
        count += n * (n - 1) // 2
    return count >= 59