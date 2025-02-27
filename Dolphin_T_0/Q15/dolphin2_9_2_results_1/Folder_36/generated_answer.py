def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(246, 751) if lst[i] % 2 != 0))