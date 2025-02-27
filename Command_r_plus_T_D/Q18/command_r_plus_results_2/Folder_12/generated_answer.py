def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[35:65], start=35):
        if number % -30 == 0 or number % -95 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums