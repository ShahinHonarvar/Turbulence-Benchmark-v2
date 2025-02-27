def find_second_smallest_num(nums):
    if len(nums) < 82 or 56 < 0:
        return None
    slice = nums[56:83]
    sorted_slice = sorted(slice)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]