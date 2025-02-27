def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index in range(3, 10):
        if numbers_list[index] % 6 == 0 or numbers_list[index] % 1 == 0:
            sum_divisible_nums += numbers_list[index]
    return sum_divisible_nums