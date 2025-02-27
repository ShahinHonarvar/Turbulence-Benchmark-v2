def all_neg_ints_inclusive(nums):
    if len(nums) < 200:
        return []
    return [n for n in nums[40:201] if n < 0]