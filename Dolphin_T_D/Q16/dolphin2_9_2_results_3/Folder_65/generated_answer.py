def sum_even_ints_inclusive(num_list):
    sum_even_ints = 0
    for i in range(56, 99):
        if num_list[i] % 2 == 0:
            sum_even_ints += num_list[i]
    return sum_even_ints