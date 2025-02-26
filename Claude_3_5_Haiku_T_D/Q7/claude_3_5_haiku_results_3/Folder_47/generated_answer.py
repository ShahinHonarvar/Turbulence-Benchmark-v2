def all_even_ints_inclusive(nums):
    if len(nums) <= 76:
        return []
    slice_range = nums[37:77]
    return [num for num in slice_range if num % 2 == 0]