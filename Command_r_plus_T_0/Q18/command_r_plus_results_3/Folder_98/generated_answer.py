def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(6):
        if numbers_list[index] % -1 == 0 or numbers_list[index] % 13 == 0:
            total_sum += numbers_list[index]
    return total_sum