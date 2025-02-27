from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        s = s.lower().replace(' ', '')
        str_dict[''.join(sorted(s))].append(s)
    pairs = 0
    for group in str_dict.values():
        if len(group) >= 3:
            pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 34