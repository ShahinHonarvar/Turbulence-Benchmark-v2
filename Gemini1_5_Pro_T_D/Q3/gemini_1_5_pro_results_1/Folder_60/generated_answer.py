def all_pos_ints_inclusive(nums):
    positives = []
    for i in range(75, 86):
        if i >= len(nums):
            break
        if nums[i] > 0:
            positives.append(nums[i])
    return positives