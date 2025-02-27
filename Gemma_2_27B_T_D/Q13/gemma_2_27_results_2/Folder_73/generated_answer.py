def find_second_largest_num(nums):
    subset = nums[19:93]
    if len(subset) < 2:
        return None
    return sorted(subset)[-2]