def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, number in enumerate(numbers_list[46:92], start=46):
        if number % 67 == 0 or number % 15 == 0:
            sum_divisible_nums += number
    return sum_divisible_nums