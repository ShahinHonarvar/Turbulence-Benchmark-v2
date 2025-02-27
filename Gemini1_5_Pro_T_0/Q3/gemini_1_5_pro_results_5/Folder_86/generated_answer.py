def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(31, 35):
        if i < len(nums) and nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints