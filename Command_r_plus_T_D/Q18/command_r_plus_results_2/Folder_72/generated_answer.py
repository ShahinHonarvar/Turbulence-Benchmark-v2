def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible = 0
    for index, num in enumerate(numbers_list[38:82], 38):
        if num % -61 == 0 or num % -71 == 0:
            sum_divisible += num
    return sum_divisible