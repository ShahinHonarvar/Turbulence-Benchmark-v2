def all_even_ints_exclusive(nums):
    out = []
    for i in range(38, 81):
        if i % 2 != 0:
            continue
        out.append(nums[i])
    return out