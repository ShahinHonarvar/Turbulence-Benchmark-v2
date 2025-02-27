def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index in range(34, 82):
        if numbers_list[index] % 27 == 0 or numbers_list[index] % 57 == 0:
            sum_divisible_nums += numbers_list[index]
    return sum_divisible_nums