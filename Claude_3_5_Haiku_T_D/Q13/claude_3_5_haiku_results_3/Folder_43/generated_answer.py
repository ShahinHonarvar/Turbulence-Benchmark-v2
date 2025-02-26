def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    slice_nums = nums[68:87]
    if len(slice_nums) == 0:
        return None
    sorted_slice = sorted(slice_nums, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None