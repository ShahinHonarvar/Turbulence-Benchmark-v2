def if_contains_anagrams(lst):
    a = [''.join(sorted(i.lower())) for i in lst if len(i) >= 3]
    return len(a) == len(set(a)) <= 255