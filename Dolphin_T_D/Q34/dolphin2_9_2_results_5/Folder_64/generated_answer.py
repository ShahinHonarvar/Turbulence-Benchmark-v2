def find_original_set(a, b, c, d, e, f, g):
    s = set(a)
    for i in b:
        if i not in s:
            s.add(i)
    for i in c:
        if i not in s:
            s.add(i)
    for i in d:
        if i not in s:
            s.add(i)
    for i in e:
        if i not in s:
            s.add(i)
    for i in f:
        if i not in s:
            s.add(i)
    for i in g:
        if i not in s:
            s.add(i)
    return s