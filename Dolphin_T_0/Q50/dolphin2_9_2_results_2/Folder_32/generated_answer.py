def if_contains_anagrams(lst):
    s = set()
    c = 0
    for str in lst:
        if len(str) >= 3:
            s.add(''.join(sorted(str.lower())))
    for i in s:
        if lst.count(i) >= 2:
            c += 1
    return c >= 194