def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(max(64, 0), min(len(nums), 67)):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints