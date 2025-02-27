def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in range(32, 36):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    if sum_even == 0:
        return 0
    else:
        return sum_even