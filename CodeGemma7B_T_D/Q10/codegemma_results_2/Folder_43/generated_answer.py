def all_odd_ints_exclusive(lst):
    rng = range(38, 77, 2)
    return [i for i in rng if i in lst and i % 2]