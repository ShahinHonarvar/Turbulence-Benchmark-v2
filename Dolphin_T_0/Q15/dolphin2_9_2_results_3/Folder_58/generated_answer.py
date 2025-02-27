def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(209, 557) if lst[i] % 2 != 0))