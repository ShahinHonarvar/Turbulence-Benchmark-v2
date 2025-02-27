def find_second_largest_num(nums):
    filtered = nums[27:56]
    if len(filtered) < 2:
        return None
    filtered.sort()
    return filtered[-2]