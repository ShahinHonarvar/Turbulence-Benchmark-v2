def all_neg_ints_inclusive(nums):
    return [i for i in range(len(nums) - 1, -1, -1) if nums[i] < 0]