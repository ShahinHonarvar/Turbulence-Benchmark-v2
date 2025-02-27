def sum_ints_div_by_either_nums(nums):
    return sum((x for x in nums[25:71] if x % 74 == 0 or x % 15 == 0))