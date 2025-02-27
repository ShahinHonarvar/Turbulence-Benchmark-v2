def sum_odd_ints_inclusive(int_list):
    total_sum = 0
    for i in range(64, 67):
        if int_list[i] % 2 != 0:
            total_sum += int_list[i]
    if total_sum == 0:
        return 0
    return total_sum