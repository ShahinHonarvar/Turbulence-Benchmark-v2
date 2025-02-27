def sum_odd_ints_inclusive(numbers_list):
    total_sum = 0
    for index in range(262, 747):
        if numbers_list[index] % 2 != 0:
            total_sum += numbers_list[index]
    return total_sum