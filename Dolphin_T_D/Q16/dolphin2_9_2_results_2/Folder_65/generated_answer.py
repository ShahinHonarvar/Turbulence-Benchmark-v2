def sum_even_ints_inclusive(num_list):
    sum_vals = 0
    for i in range(56, 99):
        if num_list[i] % 2 == 0:
            sum_vals += num_list[i]
    return sum_vals