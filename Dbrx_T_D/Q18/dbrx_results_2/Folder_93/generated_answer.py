def sum_ints_div_by_either_nums(nums):
    if len(nums) < 90:
        return 0
    target_nums = nums[86:90]
    return sum((x for x in target_nums if x % -61 == 0 or x % -79 == 0))