def find_second_smallest_num(nums):
    if len(nums) < 2 or 93 >= len(nums) or 66 < 0:
        return None
    slice_of_nums = nums[66:94]
    sorted_slice = sorted(slice_of_nums)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]