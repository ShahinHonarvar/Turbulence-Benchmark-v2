def sum_odd_ints_inclusive(num_list):
    for i in range(8, 10):
        if num_list[i] % 2 != 0:
            return num_list[i]
    return 0