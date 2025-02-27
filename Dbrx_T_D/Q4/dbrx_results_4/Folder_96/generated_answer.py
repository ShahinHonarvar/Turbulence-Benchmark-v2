def all_pos_ints_exclusive(nums):
    if len(nums) < 200:
        return []
    pos_ints = []
    for i in range(50, 200):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints