def find_second_smallest_num(nums):
    subset = sorted(nums[66:94])
    return subset[1] if len(subset) > 1 else None