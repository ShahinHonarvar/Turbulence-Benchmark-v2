def all_odd_ints_exclusive(nums):
    results = []
    for i in range(15, 40):
        if i % 2 != 0:
            results.append(nums[i])
    return results