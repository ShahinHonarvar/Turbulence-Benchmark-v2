def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i in range(71, 200):
        if i >= len(nums):
            break
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints