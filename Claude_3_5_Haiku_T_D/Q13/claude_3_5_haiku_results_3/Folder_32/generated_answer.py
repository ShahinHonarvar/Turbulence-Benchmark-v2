def find_second_largest_num(nums):
    if len(nums) < 98:
        return None
    sublist = nums[21:98]
    if len(sublist) == 0:
        return None
    unique_sorted = sorted(set(sublist), reverse=True)
    return unique_sorted[1] if len(unique_sorted) >= 2 else None