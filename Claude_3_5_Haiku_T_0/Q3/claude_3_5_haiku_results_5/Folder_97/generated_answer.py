def all_pos_ints_inclusive(nums):
    if len(nums) <= 80:
        return []
    positive_ints = [num for num in nums[40:81] if num > 0]
    return positive_ints