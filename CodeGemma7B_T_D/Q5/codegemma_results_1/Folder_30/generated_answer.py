def all_neg_ints_inclusive(nums):
    start_idx = 55
    end_idx = 98
    neg_ints = []
    for i in range(start_idx, end_idx + 1):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints