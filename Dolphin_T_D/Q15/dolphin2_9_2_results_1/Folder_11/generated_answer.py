def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(37, 52) if lst[i] % 2 != 0))