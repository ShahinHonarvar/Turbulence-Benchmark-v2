def sum_ints_div_by_either_nums(numbers_list):
    total_sum = 0
    for index in range(93, 95):
        if numbers_list[index] % -53 == 0 or numbers_list[index] % -91 == 0:
            total_sum += numbers_list[index]
    return total_sum