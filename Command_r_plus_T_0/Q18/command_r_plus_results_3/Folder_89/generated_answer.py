def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for i in range(28, 97):
        if numbers_list[i] % 90 == 0 or numbers_list[i] % 97 == 0:
            sum_divisible_nums += numbers_list[i]
    return sum_divisible_nums