def sum_even_ints_inclusive(int_list):
    sum_even_nums = 0
    for i in range(62, 100):
        if i in int_list and i % 2 == 0:
            sum_even_nums += i
    if sum_even_nums == 0:
        return 0
    else:
        return sum_even_nums