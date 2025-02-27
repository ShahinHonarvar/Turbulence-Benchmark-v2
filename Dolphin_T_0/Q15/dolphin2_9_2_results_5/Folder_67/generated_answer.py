def sum_odd_ints_inclusive(lst):
    return sum(filter(lambda x: x % 2 == 1 and 22 <= lst.index(x) <= 50, lst))