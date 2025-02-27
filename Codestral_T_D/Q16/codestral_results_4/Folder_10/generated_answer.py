def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(25, 60) if lst[i] % 2 == 0))