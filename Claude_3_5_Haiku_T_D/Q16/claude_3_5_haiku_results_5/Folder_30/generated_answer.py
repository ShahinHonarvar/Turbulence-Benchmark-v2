def sum_even_ints_inclusive(lst):
    if len(lst) <= 98:
        return 0
    even_sum = 0
    for i in range(55, 99):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum