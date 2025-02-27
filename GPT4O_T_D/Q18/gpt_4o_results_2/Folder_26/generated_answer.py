def sum_ints_div_by_either_nums(nums):
    if len(nums) < 71:
        return 0
    return sum((x for x in nums[69:71] if x % 72 == 0 or x % 70 == 0))