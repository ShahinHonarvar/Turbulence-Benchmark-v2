def sum_odd_ints_inclusive(num_list):
    total = 0
    for i in range(639, 976):
        if num_list[i] % 2 != 0:
            total += num_list[i]
    return total