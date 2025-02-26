def find_second_largest_num(nums):
    if len(nums) <= 88:
        return None
    subset = nums[75:89]
    if len(subset) < 2:
        return None
    unique_nums = sorted(set(subset), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None