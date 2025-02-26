def find_second_largest_num(nums):
    if len(nums) <= 200:
        return None
    slice_nums = nums[200:201]
    if not slice_nums:
        return None
    return slice_nums[0]