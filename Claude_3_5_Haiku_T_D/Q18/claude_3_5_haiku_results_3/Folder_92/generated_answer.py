def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 1:
        return 0
    return nums[0] if nums[0] % 1 == 0 or nums[0] % -1 == 0 else 0