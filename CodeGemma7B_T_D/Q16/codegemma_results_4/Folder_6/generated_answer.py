def sum_even_ints_inclusive(lst):
    sum_of_even_nums = 0
    for i in range(10, 67):
        if lst[i] % 2 == 0:
            sum_of_even_nums += lst[i]
    if sum_of_even_nums == 0:
        return 0
    else:
        return sum_of_even_nums