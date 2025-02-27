def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(29, 46):
        if numbers_list[index] % 27 == 0 or numbers_list[index] % 81 == 0:
            total_sum += numbers_list[index]
    return total_sum