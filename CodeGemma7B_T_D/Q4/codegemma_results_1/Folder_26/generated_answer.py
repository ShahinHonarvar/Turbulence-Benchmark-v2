def all_pos_ints_exclusive(nums):
    idx44 = nums.index(44)
    idx78 = nums.index(78)
    if idx44 > idx78:
        return []
    pos_ints = []
    for i in range(idx44, idx78):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints