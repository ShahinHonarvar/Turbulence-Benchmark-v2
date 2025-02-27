def find_second_largest_num(nums):
    subset = nums[34:56]
    if len(subset) < 2:
        return None
    return sorted(subset)[-2]