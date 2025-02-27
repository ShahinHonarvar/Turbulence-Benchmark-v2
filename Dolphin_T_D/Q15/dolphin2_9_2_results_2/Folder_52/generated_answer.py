def sum_odd_ints_inclusive(lst):
    return sum(lambda x: x % 2 == 1 and 28 <= lst.index(x) <= 38)(lst)