def sum_odd_ints_inclusive(lst):
    sublist = lst[4:5]
    return sum((i for i in sublist if i % 2 != 0))