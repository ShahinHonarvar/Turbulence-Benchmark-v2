def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[38:53], start=38):
        if number % -41 == 0 or number % -47 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums