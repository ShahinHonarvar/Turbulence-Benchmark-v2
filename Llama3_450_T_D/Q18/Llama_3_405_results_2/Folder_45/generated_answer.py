def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 30 <= i <= 200 and (num % -115 == 0 or num % 115 == 0)))