def sum_even_ints_inclusive(num_list):
    sum_even = 0
    for i in range(0, 3):
        if num_list[i] % 2 == 0:
            sum_even += num_list[i]
    return sum_even