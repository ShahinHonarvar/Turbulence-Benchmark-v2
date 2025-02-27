def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 306 <= i <= 957 and (num % 982 == 0 or num % 319 == 0)))