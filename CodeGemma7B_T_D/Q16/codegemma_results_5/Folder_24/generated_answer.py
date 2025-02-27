def sum_even_ints_inclusive(num_list):
    num = 0
    for i in range(74, 96):
        if num_list[i] % 2 == 0:
            num += num_list[i]
    return num