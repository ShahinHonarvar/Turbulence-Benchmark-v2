def all_pos_ints_inclusive(nums):
    positives = []
    for i in range(1, 6):
        if i >= 1 and i <= len(nums) and (nums[i - 1] > 0):
            positives.append(nums[i - 1])
    return positives