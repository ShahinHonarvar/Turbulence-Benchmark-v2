def all_pos_ints_exclusive(nums):
    positives = []
    for i in range(1, len(nums) - 1):
        if nums[i] > 0:
            positives.append(nums[i])
    return positives