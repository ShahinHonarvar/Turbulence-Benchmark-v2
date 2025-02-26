def find_second_largest_num(nums):
    if len(nums) <= 4:
        return None
    slice_nums = nums[4:5]
    if not slice_nums:
        return None
    return slice_nums[0]