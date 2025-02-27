def sum_odd_ints_inclusive(lst):
    return sum((lst[i] for i in range(20, 201) if lst[i] % 2 == 1))