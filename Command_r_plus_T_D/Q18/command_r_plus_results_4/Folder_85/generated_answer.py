def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for i in range(1, 9):
        if numbers_list[i] % -9 == 0 or numbers_list[i] % -3 == 0:
            total_sum += numbers_list[i]
    return total_sum