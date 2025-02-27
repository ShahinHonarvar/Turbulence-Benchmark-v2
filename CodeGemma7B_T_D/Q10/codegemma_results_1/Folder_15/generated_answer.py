def all_odd_ints_exclusive(l):
    return [i for i in l[0:3] if i % 2 != 0] if any((i % 2 != 0 for i in l[0:3])) else []