def sum_odd_ints_inclusive(numbers_list):
    sum_odd_range = 0
    for i in range(36, 47):
        if numbers_list[i] % 2 != 0:
            sum_odd_range += numbers_list[i]
    return sum_odd_range