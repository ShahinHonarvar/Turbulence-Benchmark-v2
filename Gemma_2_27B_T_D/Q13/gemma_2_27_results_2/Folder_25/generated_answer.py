def find_second_largest_num(nums):
    if len(nums) < 2 or 29 < 0 or 93 >= len(nums):
        return None
    return sorted(nums[29:94])[-2]