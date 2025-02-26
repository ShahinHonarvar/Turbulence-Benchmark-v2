def all_neg_ints_inclusive(nums):
    if len(nums) <= 200:
        return []
    return [num for num in nums[100:201] if num < 0]