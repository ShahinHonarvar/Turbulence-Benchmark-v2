def sum_even_ints_inclusive(lst):
    if len(lst) <= 86:
        return 0
    even_sum = 0
    for i in range(68, 87):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum