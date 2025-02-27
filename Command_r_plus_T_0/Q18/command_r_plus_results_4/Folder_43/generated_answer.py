def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, number in enumerate(numbers_list[57:86], start=57):
        if number % -77 == 0 or number % -32 == 0:
            sum_divisible += number
    return sum_divisible