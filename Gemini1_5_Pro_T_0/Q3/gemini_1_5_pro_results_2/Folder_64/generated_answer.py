def all_pos_ints_inclusive(nums):
    positives = []
    for i in range(min(5, len(nums))):
        if nums[i] > 0:
            positives.append(nums[i])
    return positives