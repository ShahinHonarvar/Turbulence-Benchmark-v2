def all_pos_ints_inclusive(nums):
    if len(nums) <= 538:
        return []
    result = [num for num in nums[527:539] if num > 0]
    return result