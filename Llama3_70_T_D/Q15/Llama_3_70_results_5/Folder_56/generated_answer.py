def sum_odd_ints_inclusive(lst):
    return sum((i for i in lst[:lst.index(lst[0]) + 1] if i % 2 != 0)) if lst else 0