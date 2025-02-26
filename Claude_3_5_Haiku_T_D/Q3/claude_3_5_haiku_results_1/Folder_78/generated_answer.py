def all_pos_ints_inclusive(nums):
    if len(nums) <= 51:
        return []
    result = [num for num in nums[43:52] if num > 0]
    return result