def sum_even_ints_inclusive(lst):
    total = sum((lst[i] for i in range(50, 55) if lst[i] % 2 == 0))
    return total