def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for i in range(2):
        if numbers_list[i] % 2 == 0 or numbers_list[i] == 1:
            total_sum += numbers_list[i]
    return total_sum