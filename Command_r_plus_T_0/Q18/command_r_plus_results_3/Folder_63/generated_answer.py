def sum_ints_div_by_either_nums(numbers_list):
    sum_divisible = 0
    for i in range(31, 51):
        if numbers_list[i] % 81 == 0 or numbers_list[i] % 64 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible