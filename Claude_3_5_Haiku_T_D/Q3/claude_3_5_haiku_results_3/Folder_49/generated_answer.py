def all_pos_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    return [num for num in nums[80:201] if num > 0]