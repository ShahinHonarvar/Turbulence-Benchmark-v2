def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(90, 201):
        if i in range(len(nums)) and nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints