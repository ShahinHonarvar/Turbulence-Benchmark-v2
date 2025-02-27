def find_second_smallest_num(nums):
    subset = nums[22:89]
    if len(subset) < 2:
        return None
    subset = sorted(subset)
    return subset[1] if subset[1] != subset[0] else None