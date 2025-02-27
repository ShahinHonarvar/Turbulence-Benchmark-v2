def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, number in enumerate(numbers_list[281:695], start=281):
        if number % -722 == 0 or number % -731 == 0:
            sum_divisible += number
    return sum_divisible