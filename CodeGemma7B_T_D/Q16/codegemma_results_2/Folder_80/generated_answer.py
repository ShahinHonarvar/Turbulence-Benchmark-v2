def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(64, 67):
        if lst[i] % 2 == 0:
            sum_even += lst[i]
    if sum_even == 0:
        return sum_even
    else:
        return sum_even