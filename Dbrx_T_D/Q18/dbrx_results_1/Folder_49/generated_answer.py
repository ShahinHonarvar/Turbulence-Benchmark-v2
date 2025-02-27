def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[80:201] if n % 10 == 0 or n % 1000 == 0))