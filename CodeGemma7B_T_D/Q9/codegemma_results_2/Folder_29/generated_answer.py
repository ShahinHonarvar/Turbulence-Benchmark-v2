def all_odd_ints_inclusive(nums):
    results = []
    for i in range(59, 98):
        if i % 2 != 0:
            results.append(nums[i])
    return results