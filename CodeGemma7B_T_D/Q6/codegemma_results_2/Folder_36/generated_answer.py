def all_neg_ints_exclusive(nums):
    result = []
    for i in range(598, 767):
        if nums[i] < 0 and i not in range(598, 768):
            result.append(nums[i])
    return result