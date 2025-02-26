def find_second_smallest_num(nums):
    if len(nums) < 41:
        return None
    sublist = nums[28:41]
    if len(sublist) < 2:
        return None
    unique_sorted = sorted(set(sublist))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None