def sum_even_ints_inclusive(num_list):
    sum_int = 0
    for i in range(639, 976):
        if num_list[i] % 2 == 0:
            sum_int += num_list[i]
    return sum_int