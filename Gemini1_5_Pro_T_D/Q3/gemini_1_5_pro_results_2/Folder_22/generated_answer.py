def all_pos_ints_inclusive(nums):
    positives = []
    for i in range(40, 201):
        if i >= len(nums):
            break
        if nums[i] > 0:
            positives.append(nums[i])
    return positives