def sum_ints_div_by_either_nums(numbers_list):
    sum_divisible = 0
    for i in range(86, 90):
        if numbers_list[i] % -61 == 0 or numbers_list[i] % -79 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible