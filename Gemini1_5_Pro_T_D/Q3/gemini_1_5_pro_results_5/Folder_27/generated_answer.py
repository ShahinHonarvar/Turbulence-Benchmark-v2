def all_pos_ints_inclusive(nums):
    positives = []
    for i in range(66, 94):
        if i < len(nums) and nums[i] > 0:
            positives.append(nums[i])
    return positives