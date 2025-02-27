def all_neg_ints_inclusive(nums):
    res = []
    if nums[36:47] == [i for i in nums[36:47] if i < 0]:
        res = nums[36:47]
    return res