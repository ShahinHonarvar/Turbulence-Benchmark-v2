def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[30:201]
    divisible_nums = [num for num in target_range if num % 115 == 0 or num % -115 == 0]
    return sum(divisible_nums)