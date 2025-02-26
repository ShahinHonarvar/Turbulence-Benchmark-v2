def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    slice_nums = nums[82:87]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(slice_nums)
    return sorted_slice[1]