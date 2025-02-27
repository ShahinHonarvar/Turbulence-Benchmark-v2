def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(40, 81) if lst[i] % 2 != 0))