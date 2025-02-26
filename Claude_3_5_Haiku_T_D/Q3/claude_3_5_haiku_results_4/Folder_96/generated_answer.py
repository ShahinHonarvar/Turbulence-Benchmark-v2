def all_pos_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    result = [num for num in nums[50:201] if num > 0]
    return result