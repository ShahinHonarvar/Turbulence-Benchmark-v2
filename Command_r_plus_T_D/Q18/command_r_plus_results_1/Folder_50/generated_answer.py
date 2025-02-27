def sum_ints_div_by_either_nums(numbers_list):
    sum_divisible = 0
    for i in range(46, 92):
        if numbers_list[i] % 67 == 0 or numbers_list[i] % 15 == 0:
            sum_divisible += numbers_list[i]
    return sum_divisible