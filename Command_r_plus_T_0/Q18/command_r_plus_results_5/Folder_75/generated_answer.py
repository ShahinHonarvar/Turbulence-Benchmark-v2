def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for index in range(20, 94):
        if numbers_list[index] % -92 == 0 or numbers_list[index] % -50 == 0:
            total_sum += numbers_list[index]
    return total_sum