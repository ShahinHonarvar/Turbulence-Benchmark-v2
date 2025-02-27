def sum_even_ints_inclusive(lst):
    return sum((lst[i] for i in range(30, 201) if lst[i] % 2 == 0))