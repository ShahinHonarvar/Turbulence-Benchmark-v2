def sum_even_ints_inclusive(num_list):
    sum_even = 0
    for i in range(75, 86):
        if i < len(num_list):
            if num_list[i] % 2 == 0:
                sum_even += num_list[i]
    return sum_even