def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    slice_nums = nums[0:3]
    sorted_slice = sorted(slice_nums)
    if len(sorted_slice) > 1:
        return sorted_slice[1]
    else:
        return None