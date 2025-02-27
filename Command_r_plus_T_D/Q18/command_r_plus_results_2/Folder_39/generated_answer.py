def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[13:77], start=13):
        if number % -66 == 0 or number % -32 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums