def if_contains_anagrams(lst):
    lst = [s for s in lst if len(s) >= 3]
    lst = [''.join(sorted(s.lower())) for s in lst if s.isalpha()]
    return len(lst) - len(set(lst)) <= 255