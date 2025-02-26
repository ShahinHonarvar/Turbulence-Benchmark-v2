def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[58:76]
    divisible_nums = [num for num in target_range if num % 72 == 0 or num % 62 == 0]
    return sum(divisible_nums)