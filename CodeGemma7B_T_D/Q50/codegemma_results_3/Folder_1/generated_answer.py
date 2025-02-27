from itertools import product

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    str_list = [s for s in str_list if len(s) >= 3]
    anagrams = {''.join(p): [] for p in product('abcdefghijklmnopqrstuvwxyz', repeat=len(str_list[0]))}
    for s in str_list:
        for key in anagrams:
            if sorted(key) == sorted(s):
                anagrams[key].append(s)
    return len([k for k in anagrams.values() if len(k) >= 96]) > 0