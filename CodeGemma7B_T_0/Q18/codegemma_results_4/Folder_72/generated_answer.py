def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[38:82] if num % 61 == 0 or num % 71 == 0)) or 0