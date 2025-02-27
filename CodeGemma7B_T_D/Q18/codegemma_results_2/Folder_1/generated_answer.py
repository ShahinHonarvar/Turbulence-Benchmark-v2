def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[10:29] if x % 61 == 0 or x % 64 == 0)) or 0