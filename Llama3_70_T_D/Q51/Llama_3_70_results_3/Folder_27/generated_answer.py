def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.casefold())) for s in lst if s.isascii() and len(s) >= 3]
    return len(lst) - len(set(lst)) <= 113