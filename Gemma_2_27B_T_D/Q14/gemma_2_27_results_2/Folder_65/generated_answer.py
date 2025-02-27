def find_second_smallest_num(nums):
    if len(nums) < 57 or 56 < 0:
        return None
    slice_nums = nums[56:58]
    if len(slice_nums) < 2:
        return None
    return sorted(slice_nums)[1]