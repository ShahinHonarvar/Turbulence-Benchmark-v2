def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[828:933], start=828):
        if number % -649 == 0 or number % -461 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums