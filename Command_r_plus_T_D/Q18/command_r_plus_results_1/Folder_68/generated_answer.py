def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(7, len(numbers_list)):
        if numbers_list[index] % 5 == 0 or numbers_list[index] % 7 == 0:
            total_sum += numbers_list[index]
    return total_sum