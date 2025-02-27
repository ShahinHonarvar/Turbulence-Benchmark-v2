def all_neg_ints_inclusive(nums):
    if not nums or len(nums) < 49:
        return []
    for i in range(35, 50):
        if nums[i] < 0:
            return nums[i:50]
    return []