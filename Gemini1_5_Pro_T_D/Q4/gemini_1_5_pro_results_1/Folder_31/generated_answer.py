def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i in range(87, 95):
        if i >= len(nums) or i < 0:
            break
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints