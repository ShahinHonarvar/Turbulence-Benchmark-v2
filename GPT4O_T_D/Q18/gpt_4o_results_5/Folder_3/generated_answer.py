def sum_ints_div_by_either_nums(nums):
    if len(nums) < 53:
        return 0
    return sum((x for x in nums[38:53] if x % -41 == 0 or x % -47 == 0))