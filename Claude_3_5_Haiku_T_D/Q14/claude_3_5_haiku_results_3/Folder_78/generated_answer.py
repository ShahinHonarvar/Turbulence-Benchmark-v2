def find_second_smallest_num(nums):
    if len(nums) < 79:
        return None
    slice_nums = nums[17:79]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(set(slice_nums))
    return sorted_slice[1] if len(sorted_slice) >= 2 else None