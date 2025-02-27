def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, number in enumerate(numbers_list[68:100], start=68):
        if number % -37 == 0 or number % -26 == 0:
            sum_divisible += number
    return sum_divisible