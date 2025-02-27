def sum_odd_ints_inclusive(numbers_list):
    sum_odd_range = 0
    for index in range(36, 47):
        if numbers_list[index] % 2 != 0:
            sum_odd_range += numbers_list[index]
    return sum_odd_range