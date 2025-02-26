def find_second_smallest_num(nums):
    if not nums or len(nums) < 688:
        return None
    slice_nums = nums[686:988]
    if len(slice_nums) < 2:
        return None
    unique_nums = sorted(set(slice_nums))
    return unique_nums[1] if len(unique_nums) >= 2 else None