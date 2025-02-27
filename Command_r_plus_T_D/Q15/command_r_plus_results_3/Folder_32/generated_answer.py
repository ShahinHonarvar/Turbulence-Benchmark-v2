def sum_odd_ints_inclusive(numbers_list):
    total_sum = 0
    for idx in range(21, 98):
        if numbers_list[idx] % 2 != 0:
            total_sum += numbers_list[idx]
    return total_sum