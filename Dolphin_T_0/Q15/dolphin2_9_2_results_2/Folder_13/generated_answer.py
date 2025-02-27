def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(25, 88) if lst[i] % 2 != 0))