def sum_odd_ints_inclusive(numbers_list):
    total_sum = 0
    for i in range(25, 88):
        if numbers_list[i] % 2 != 0:
            total_sum += numbers_list[i]
    return total_sum