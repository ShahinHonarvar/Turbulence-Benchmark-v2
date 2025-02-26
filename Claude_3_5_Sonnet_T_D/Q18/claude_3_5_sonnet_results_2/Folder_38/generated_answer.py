def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[10:77]
    divisible_nums = [num for num in target_range if num % -40 == 0 or num % -12 == 0]
    return sum(divisible_nums)