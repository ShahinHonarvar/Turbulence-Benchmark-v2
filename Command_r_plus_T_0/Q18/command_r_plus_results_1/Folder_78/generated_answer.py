def sum_ints_div_by_either_nums(numbers_list):
    total_sum = 0
    for i in range(34, 70):
        if numbers_list[i] % 19 == 0 or numbers_list[i] % 32 == 0:
            total_sum += numbers_list[i]
    return total_sum