def sum_even_ints_inclusive(int_list):
    sum_even_nums = 0
    for i in range(50, 55):
        if i < len(int_list) and int_list[i] % 2 == 0:
            sum_even_nums += int_list[i]
    return sum_even_nums