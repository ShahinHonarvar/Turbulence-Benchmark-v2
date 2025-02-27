def all_neg_ints_exclusive(nums):
    for i in range(743, 867):
        if nums[i] < 0:
            yield nums[i]