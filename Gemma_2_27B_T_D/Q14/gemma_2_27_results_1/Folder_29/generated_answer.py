def find_second_smallest_num(nums):
    if len(nums) < 98 or 55 < 0:
        return None
    slice_nums = nums[55:99]
    if len(slice_nums) > 1:
        return sorted(slice_nums)[1]
    return None