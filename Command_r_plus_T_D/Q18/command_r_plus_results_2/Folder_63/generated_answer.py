def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for i in range(31, 51):
        if numbers_list[i] % 81 == 0 or numbers_list[i] % 64 == 0:
            sum_divisible_nums += numbers_list[i]
    return sum_divisible_nums