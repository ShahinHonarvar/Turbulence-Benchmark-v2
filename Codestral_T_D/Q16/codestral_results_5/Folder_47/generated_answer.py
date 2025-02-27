def sum_even_ints_inclusive(lst):
    even_sum = sum((lst[i] for i in range(37, 77) if lst[i] % 2 == 0))
    return even_sum