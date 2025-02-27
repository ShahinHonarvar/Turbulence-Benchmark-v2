def find_second_largest_num(nums):
    specific_range = nums[34:56]
    if len(specific_range) < 2:
        return None
    else:
        unique_nums = set(specific_range)
        return sorted(unique_nums)[-2] if len(unique_nums) >= 2 else None