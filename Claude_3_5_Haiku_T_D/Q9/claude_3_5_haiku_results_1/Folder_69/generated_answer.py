def all_odd_ints_inclusive(nums):
    if len(nums) <= 35:
        return []
    slice_range = nums[32:36]
    return [num for num in slice_range if num % 2 != 0]