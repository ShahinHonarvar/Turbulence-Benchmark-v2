def sum_ints_div_by_either_nums(nums):
    s = sum((num for num in nums[10:29] if num % 61 == 0 or num % 64 == 0))
    return s if s else 0