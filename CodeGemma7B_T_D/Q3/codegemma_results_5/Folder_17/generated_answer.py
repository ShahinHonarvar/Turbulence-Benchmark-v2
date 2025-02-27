def all_pos_ints_inclusive(nums):
    out = []
    for num in nums[62:79]:
        if num > 0:
            out.append(num)
    return out or []