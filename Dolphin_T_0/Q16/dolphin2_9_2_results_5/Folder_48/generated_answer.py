def sum_even_ints_inclusive(in_list):
    sum_even = 0
    for i in range(533, 606):
        if in_list[i] % 2 == 0:
            sum_even += in_list[i]
    return sum_even