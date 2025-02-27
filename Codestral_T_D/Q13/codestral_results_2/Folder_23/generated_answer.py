def find_second_largest_num(nums):
    subset = sorted(set(nums[52:72]), reverse=True)
    return subset[1] if len(subset) > 1 else None