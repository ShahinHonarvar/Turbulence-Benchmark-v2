def all_even_ints_exclusive(l):
    l = l[:3]
    if l == []:
        return []
    t = [x for x in l if x % 2 == 0]
    if t == []:
        return []
    return t