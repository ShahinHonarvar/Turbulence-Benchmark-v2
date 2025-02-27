def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(60, 201) if lst[i] % 2 != 0))