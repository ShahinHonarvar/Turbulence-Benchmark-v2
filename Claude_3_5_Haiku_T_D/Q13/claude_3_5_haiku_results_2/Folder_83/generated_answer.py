def find_second_largest_num(nums):
    if len(nums) < 2 or 90 >= len(nums):
        return None
    slice_nums = nums[90:91]
    if not slice_nums:
        return None
    return sorted(slice_nums, reverse=True)[1] if len(slice_nums) > 1 else None