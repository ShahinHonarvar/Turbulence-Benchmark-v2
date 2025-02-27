def sum_odd_ints_inclusive(numbers_list):
    odd_sum = 0
    for i in range(74, 96):
        if numbers_list[i] % 2 != 0:
            odd_sum += numbers_list[i]
    return odd_sum