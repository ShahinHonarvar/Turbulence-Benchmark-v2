def sum_even_ints_inclusive(int_list):
    if len(int_list) < 92:
        return 0
    sum_even = 0
    for i in range(19, 93):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even