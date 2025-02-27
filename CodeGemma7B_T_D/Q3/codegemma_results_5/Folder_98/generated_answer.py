def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(7):
        if i >= 1 and i <= 6 and (nums[i] > 0):
            pos_ints.append(nums[i])
    return pos_ints