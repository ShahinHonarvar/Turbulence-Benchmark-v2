def find_second_smallest_num(nums):
    if 23 >= len(nums):
        return None
    indices = nums[23:24]
    if len(indices) != 1:
        return None
    return sorted(indices)[1] if len(indices) > 1 else None