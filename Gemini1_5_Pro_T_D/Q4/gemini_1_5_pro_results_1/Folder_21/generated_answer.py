def all_pos_ints_exclusive(nums):
    positives = []
    for i in range(743, 867):
        if i < len(nums) and nums[i] > 0:
            positives.append(nums[i])
    return positives