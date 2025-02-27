def sum_even_ints_inclusive(num_list):
    if not num_list:
        return 0
    total = 0
    for i in range(22, 64):
        if i % 2 == 0:
            total += num_list[i]
    return total