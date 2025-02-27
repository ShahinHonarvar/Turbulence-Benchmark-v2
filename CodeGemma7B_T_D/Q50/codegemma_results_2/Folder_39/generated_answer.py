from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        key = ''.join(sorted(s.lower().replace(' ', '')))
        if len(key) >= 3:
            str_dict[key].append(s)
    return len(list(filter(lambda x: len(x) >= 54, str_dict.values()))) > 0