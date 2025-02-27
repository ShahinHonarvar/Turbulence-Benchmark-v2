def all_pos_ints_inclusive(nums):
    out = []
    for i in range(23, 24):
        if nums[i] > 0:
            out.append(nums[i])
    return out or []