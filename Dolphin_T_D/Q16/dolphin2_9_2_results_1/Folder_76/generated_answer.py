def sum_even_ints_inclusive(lst):
    sum_nums = 0
    for i in range(686, 988):
        if lst[i] % 2 == 0:
            sum_nums += lst[i]
    return sum_nums