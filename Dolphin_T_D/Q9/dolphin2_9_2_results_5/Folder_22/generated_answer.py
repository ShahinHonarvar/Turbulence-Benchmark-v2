def all_odd_ints_inclusive(lst):
    return [n for i, n in enumerate(lst) if i in range(40, 201) and n % 2 == 1]