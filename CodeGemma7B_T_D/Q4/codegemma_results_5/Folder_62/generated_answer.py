def all_pos_ints_exclusive(nums):
    out = []
    for i in range(55, 84):
        if nums[i] > 0:
            out.append(nums[i])
    return out