def all_pos_ints_inclusive(nums):
    out = []
    for i in range(1, 6):
        try:
            if nums[i] > 0:
                out.append(nums[i])
        except IndexError:
            pass
    return out