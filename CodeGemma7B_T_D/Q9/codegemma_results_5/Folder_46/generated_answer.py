def all_odd_ints_inclusive(nums):
    out = []
    for i in range(30, 88):
        if i % 2 != 0:
            out.append(nums[i])
    if out == []:
        return []
    else:
        return out