def sum_ints_div_by_either_nums(numbers_list):
    total_sum = 0
    for index in range(10, 101):
        if numbers_list[index] % 10 == 0 or numbers_list[index] % 100 == 0:
            total_sum += numbers_list[index]
    return total_sum