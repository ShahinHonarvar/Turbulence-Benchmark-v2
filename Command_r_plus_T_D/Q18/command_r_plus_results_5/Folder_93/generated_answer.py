def sum_ints_div_by_either_nums(numbers_list):
    sum_divisible_nums = 0
    for index in range(86, 90):
        if numbers_list[index] % -61 == 0 or numbers_list[index] % -79 == 0:
            sum_divisible_nums += numbers_list[index]
    return sum_divisible_nums