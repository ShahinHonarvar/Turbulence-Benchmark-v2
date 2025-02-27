def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(25, 88):
        if i % 2 == 0:
            sum_even += lst[i]
    if sum_even == 0:
        return 0
    return sum_even