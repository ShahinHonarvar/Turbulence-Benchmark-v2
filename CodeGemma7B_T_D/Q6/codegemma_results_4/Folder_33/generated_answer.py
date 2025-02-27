def all_neg_ints_exclusive(nums):
    l = []
    for i in range(369, 983):
        if nums[i] < 0 and i not in range(369, 983, -1):
            l.append(nums[i])
    return l or []