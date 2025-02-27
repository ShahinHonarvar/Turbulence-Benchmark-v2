def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[55:85], start=55):
        if number % -24 == 0 or number % -11 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums