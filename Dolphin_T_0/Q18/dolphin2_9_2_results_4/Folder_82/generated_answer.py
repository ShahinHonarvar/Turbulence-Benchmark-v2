def sum_ints_div_by_either_nums(nums_list):
    return sum((n for n in nums_list[20:201] if n % -20 == 0 or n % -200 == 0))