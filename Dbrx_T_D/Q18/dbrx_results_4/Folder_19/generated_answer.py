def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[1:4 + 1] if x % 4 == 0 or x % -6 == 0))