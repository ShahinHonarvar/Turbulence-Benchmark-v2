def all_odd_ints_inclusive(nums):
    if len(nums) <= 538:
        return []
    slice_range = nums[527:539]
    return [num for num in slice_range if num % 2 != 0]