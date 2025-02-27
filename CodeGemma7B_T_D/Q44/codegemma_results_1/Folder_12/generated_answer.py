def composite_nums_between_indices(l):
    comp = set()
    for i in range(51, 87):
        if i in l and l.index(i) >= 51 and (l.index(i) <= 86) and (not isprime(i)):
            comp.add(i)
    return comp