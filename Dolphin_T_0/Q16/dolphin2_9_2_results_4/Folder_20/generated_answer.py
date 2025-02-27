def sum_even_ints_inclusive(input_list):
    sum_even_nums = 0
    for i in range(56, 67):
        if i < len(input_list):
            if input_list[i] % 2 == 0:
                sum_even_nums += input_list[i]
    return sum_even_nums