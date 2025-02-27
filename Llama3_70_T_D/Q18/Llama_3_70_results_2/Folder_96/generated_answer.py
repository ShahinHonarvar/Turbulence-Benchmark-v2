def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[50:201], 50) if num % -34 == 0 or num % 64 == 0))