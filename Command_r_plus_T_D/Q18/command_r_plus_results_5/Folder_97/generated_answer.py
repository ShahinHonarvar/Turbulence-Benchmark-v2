def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(58, 76):
        if numbers_list[index] % 72 == 0 or numbers_list[index] % 62 == 0:
            total_sum += numbers_list[index]
    return total_sum