def all_pos_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    positive_sublist = [x for x in nums[40:201] if x > 0]
    return positive_sublist