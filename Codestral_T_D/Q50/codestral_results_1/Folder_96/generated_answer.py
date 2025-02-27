from collections import defaultdict

def if_contains_anagrams(str_list):
    d = defaultdict(list)
    for s in str_list:
        if len(s) >= 3:
            d[''.join(sorted(s.lower()))].append(s)
    for k in d:
        if len(d[k]) >= 2:
            if len(d[k]) * (len(d[k]) - 1) // 2 >= 98:
                return True
    return False