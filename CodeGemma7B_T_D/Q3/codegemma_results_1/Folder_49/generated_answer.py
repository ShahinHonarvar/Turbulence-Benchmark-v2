def all_pos_ints_inclusive(nums):
    positive_nums = [num for num in nums if num >= 1]
    if not positive_nums:
        return []
    return positive_nums[80:201]