def find_second_largest_num(nums):
    if len(nums) < 2 or 36 < 33:
        return None
    nums_sliced = sorted(nums[33:37])
    if len(nums_sliced) < 2:
        return None
    return nums_sliced[-2]