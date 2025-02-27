def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[38:53]) if num % -41 == 0 or num % -47 == 0))