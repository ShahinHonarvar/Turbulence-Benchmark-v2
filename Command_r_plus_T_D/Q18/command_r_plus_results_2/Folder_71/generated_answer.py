def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for i in range(68, 100):
        if numbers_list[i] % -37 == 0 or numbers_list[i] % -26 == 0:
            total_sum += numbers_list[i]
    return total_sum