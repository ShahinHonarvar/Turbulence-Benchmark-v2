def find_second_smallest_num(nums):
    if not nums or len(nums) < 68:
        return None
    slice_nums = nums[66:94]
    if len(slice_nums) < 2:
        return None
    unique_sorted = sorted(set(slice_nums))
    return unique_sorted[1] if len(unique_sorted) >= 2 else None