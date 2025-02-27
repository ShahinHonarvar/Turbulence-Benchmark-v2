def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[40:201], start=40):
        if number % 21 == 0 or number % 71 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums