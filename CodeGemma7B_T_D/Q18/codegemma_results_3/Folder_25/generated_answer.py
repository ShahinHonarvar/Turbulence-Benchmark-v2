def sum_ints_div_by_either_nums(nums):
    return sum((n for n in nums[25:81] if not n % 20 or not n % 26)) or 0