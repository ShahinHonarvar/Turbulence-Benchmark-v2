def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, num in enumerate(numbers_list[36:86], start=36):
        if num % -27 == 0 or num % -96 == 0:
            sum_divisible_nums += num
    return sum_divisible_nums