def all_neg_ints_inclusive(a):
    return [x for x in range(len(a)) if a[x] in range(-len(a), 0)]