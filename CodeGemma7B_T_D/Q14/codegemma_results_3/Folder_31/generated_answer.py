def find_second_smallest_num(nums):
    if len(nums) <= 29 or len(nums) > 93:
        return None
    nums_copy = sorted(nums[29:94])
    if len(nums_copy) < 2:
        return None
    return nums_copy[1]