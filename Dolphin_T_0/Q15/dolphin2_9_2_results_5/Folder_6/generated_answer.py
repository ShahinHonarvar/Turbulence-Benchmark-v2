def sum_odd_ints_inclusive(lst):
    return sum((lst[x] for x in range(10, 67) if lst[x] % 2 != 0))