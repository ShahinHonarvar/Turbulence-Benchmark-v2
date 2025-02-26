def all_pos_ints_inclusive(nums):
    if len(nums) <= 370:
        return []
    result = [num for num in nums[310:371] if num > 0]
    return result