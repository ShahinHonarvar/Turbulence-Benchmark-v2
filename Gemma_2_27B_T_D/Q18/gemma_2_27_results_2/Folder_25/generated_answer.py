def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[25:81] if n % -20 == 0 or n % -26 == 0))