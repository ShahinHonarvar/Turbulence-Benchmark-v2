def all_pos_ints_inclusive(nums):
    out = []
    for i in range(10):
        if i in nums:
            out.append(i)
    return out