def all_odd_ints_inclusive(nums):
    out = []
    for i in range(6, 7):
        if nums[i] % 2 == 1:
            out.append(nums[i])
    if out == []:
        return []
    return out