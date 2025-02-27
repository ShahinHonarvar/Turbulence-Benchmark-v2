def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(686, 988) if lst[i] % 2 != 0))