def sum_ints_div_by_either_nums(nums):
    if len(nums) < 33:
        return 0
    return sum((x for x in nums[32:100] if x % -11 == 0 or x % -15 == 0))