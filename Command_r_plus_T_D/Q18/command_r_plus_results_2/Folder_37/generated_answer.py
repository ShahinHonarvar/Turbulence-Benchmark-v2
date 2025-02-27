def sum_ints_div_by_either_nums(numbers_list: list[int]) -> int:
    sum_divisible_nums = 0
    for num in numbers_list[2:8]:
        if num % -1 == 0 or num % -7 == 0:
            sum_divisible_nums += num
    return sum_divisible_nums