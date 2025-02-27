def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, num in enumerate(numbers_list[13:77], start=13):
        if num % -66 == 0 or num % -32 == 0:
            sum_divisible += num
    return sum_divisible