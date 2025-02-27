def find_second_largest_num(nums):
    if len(nums) <= 92:
        return None
    subset = nums[12:93]
    if len(subset) < 2:
        return None
    unique_nums = list(set(subset))
    unique_nums.sort()
    return unique_nums[-2] if len(unique_nums) >= 2 else None