def all_odd_ints_inclusive(nums):
    for i in range(35, 50):
        if i % 2 != 0:
            if nums[i] not in results:
                results.append(nums[i])
    return results