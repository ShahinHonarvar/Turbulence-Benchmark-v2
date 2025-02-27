from collections import defaultdict

def if_contains_anagrams(list):
    dict = defaultdict(list)
    for i in list:
        if len(i) < 3:
            continue
        dict[''.join(sorted(i.lower()))].append(i)
    for i in dict.values():
        if len(i) >= 314:
            return True
    return False