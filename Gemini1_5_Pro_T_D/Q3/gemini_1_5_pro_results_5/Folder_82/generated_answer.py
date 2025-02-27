def all_pos_ints_inclusive(nums):
    result = []
    if len(nums) >= 201:
        result = [num for num in nums[20:201] if num > 0]
    return result