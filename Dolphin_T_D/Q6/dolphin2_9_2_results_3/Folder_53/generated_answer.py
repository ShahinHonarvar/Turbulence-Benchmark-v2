def all_neg_ints_exclusive(nums):
    result = [i for i in nums[100:200] if i < 0]
    if len(result) == 0:
        return []
    return result