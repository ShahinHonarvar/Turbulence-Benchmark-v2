def sum_odd_ints_inclusive(int_list):
    total_sum = 0
    for idx in range(60, 201):
        if int_list[idx] % 2 != 0:
            total_sum += int_list[idx]
    return total_sum