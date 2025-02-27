def sum_ints_div_by_either_nums(numbers_list):
    sum_divisible = 0
    for i in range(55, 67):
        if numbers_list[i] % 22 == 0 or numbers_list[i] % 82 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible