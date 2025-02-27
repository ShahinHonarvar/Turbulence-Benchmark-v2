def find_original_set(*sets):
    a, b = (sets[0], sets[1])
    a_b = a.union(b)
    c = next(iter(sets[2:]))
    return a_b.union(c)