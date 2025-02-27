def sum_ints_div_by_either_nums(nums):
    if len(nums) < 2:
        return 0
    return sum((x for x in nums[0:2] if x % 2 == 0 or x % 1 == 0))