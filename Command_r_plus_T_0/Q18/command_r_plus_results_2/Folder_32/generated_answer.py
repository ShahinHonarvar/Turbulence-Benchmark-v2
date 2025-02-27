def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(25, 96):
        if numbers_list[index] % 51 == 0 or numbers_list[index] % 77 == 0:
            total_sum += numbers_list[index]
    return total_sum