def sum_ints_div_by_either_nums(nums):
    return sum((n for i, n in enumerate(nums) if 306 <= i <= 957 and (n % 982 == 0 or n % 319 == 0)))