from itertools import permutations

def if_contains_anagrams(arr):
    str_dict = {}
    for s in arr:
        str_dict.setdefault(tuple(sorted([word for word in s.lower() if word.isalpha()])), []).append(s)
    return len([[y for y in x] for x in str_dict.values() if len(x) > 3]) >= 66