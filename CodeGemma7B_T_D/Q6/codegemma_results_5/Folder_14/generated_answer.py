def all_neg_ints_exclusive(nums):
    if not any((x < 0 for x in nums[1:8])):
        return []
    return [x for x in nums if x < 0 and 1 < nums.index(x) < 8]