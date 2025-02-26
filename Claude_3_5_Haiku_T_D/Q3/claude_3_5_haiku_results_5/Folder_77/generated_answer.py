def all_pos_ints_inclusive(nums):
    if len(nums) <= 538:
        return []
    positive_slice = nums[527:539]
    return [num for num in positive_slice if num > 0]