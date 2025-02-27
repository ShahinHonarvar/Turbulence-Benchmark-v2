def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for idx in range(299, 383):
        if numbers_list[idx] % 858 == 0 or numbers_list[idx] % 952 == 0:
            sum_divisible_nums += numbers_list[idx]
    return sum_divisible_nums