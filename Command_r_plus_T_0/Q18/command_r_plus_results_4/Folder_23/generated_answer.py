def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[69:98], start=69):
        if number % -90 == 0 or number % -67 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums