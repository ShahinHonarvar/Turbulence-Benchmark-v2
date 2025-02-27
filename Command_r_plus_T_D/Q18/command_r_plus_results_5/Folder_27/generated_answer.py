def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, num in enumerate(numbers_list[20:36], start=20):
        if num % -36 == 0 or num % -89 == 0:
            sum_divisible_nums += num
    return sum_divisible_nums