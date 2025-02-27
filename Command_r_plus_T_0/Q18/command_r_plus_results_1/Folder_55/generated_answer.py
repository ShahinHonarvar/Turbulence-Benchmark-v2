def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    total_sum = 0
    for idx in range(10):
        if numbers_list[idx] % 10 == 0 or numbers_list[idx] % 100 == 0:
            total_sum += numbers_list[idx]
    return total_sum