def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for index, num in enumerate(numbers_list[306:958], start=306):
        if num % 982 == 0 or num % 319 == 0:
            sum_divisible_nums += num
    return sum_divisible_nums