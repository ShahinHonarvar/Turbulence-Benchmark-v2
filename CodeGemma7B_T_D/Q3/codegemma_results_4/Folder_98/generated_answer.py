def all_pos_ints_inclusive(nums):
    out = []
    for num in nums:
        if num > 0 and num <= 6:
            out.append(num)
    return out if len(out) else []