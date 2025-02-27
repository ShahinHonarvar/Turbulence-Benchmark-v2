def find_second_largest_num(nums):
    if len(nums) < 65 or len(set(nums[29:94])) < 2:
        return None
    return sorted(nums[29:94])[-2]