def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(62, 64):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    if even_sum == 0:
        return 0
    else:
        return even_sum