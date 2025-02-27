def if_contains_anagrams(k):
    k = [i.lower() for i in k if len(i) >= 3]
    s = set()
    c = set()
    for i in k:
        s.add(''.join(sorted(i)))
    for i in s:
        c.add(k.count(i))
    return 57 >= len({i for i in c if i > 1})