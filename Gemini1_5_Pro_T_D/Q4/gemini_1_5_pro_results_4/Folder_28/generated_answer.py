def all_pos_ints_exclusive(nums):
    positives = []
    for i in range(21, 51):
        if i >= len(nums):
            break
        if nums[i] > 0:
            positives.append(nums[i])
    return positives