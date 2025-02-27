def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, num in enumerate(numbers_list[48:60], 48):
        if num % 88 == 0 or num % 58 == 0:
            sum_divisible += num
    return sum_divisible