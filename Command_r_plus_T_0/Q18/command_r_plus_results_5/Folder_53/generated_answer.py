def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for i in range(200, len(numbers_list)):
        if numbers_list[i] % 17 == 0 or numbers_list[i] % -5 == 0:
            total_sum += numbers_list[i]
    return total_sum