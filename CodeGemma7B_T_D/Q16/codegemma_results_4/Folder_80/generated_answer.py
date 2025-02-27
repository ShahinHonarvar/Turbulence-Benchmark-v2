def sum_even_ints_inclusive(num_list):
    sum_of_nums = 0
    for i in range(64, 67):
        if num_list[i] % 2 == 0:
            sum_of_nums += num_list[i]
    return sum_of_nums