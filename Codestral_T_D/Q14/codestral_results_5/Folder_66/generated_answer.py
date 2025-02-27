def find_second_smallest_num(nums):
    if 62 <= len(nums) <= 99:
        subset = sorted(nums[62:100])
        return subset[1] if len(subset) > 1 else None
    return None