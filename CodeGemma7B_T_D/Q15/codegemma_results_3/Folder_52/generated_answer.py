def sum_odd_ints_inclusive(num_list):
    total_sum = 0
    for i in range(28, 39):
        if num_list[i] % 2 != 0:
            total_sum += num_list[i]
    if total_sum == 0:
        return 0
    return total_sum