def sum_odd_ints_inclusive(numbers_list):
    odd_sum = 0
    for index in range(56, 99):
        if numbers_list[index] % 2 != 0:
            odd_sum += numbers_list[index]
    return odd_sum