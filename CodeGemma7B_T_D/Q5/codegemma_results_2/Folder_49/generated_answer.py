def all_neg_ints_inclusive(nums):
    results = []
    for i in range(80, 201):
        if nums[i] < 0:
            results.append(nums[i])
    return results