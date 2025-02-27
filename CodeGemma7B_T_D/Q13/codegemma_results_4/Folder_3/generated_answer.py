def find_second_largest_num(nums):
    if len(nums) < 63 or max(nums) < nums[62]:
        return None
    nums = sorted(nums[62:93])
    return nums[-2] or None