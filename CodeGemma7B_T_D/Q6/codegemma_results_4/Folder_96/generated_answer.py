def all_neg_ints_exclusive(nums):
    out = []
    for i in range(50, 200):
        if nums[i] < 0:
            out.append(nums[i])
    return out if out else []