def all_odd_ints_inclusive(nums):
    results = []
    for i in range(43, 87):
        if i in nums:
            if i % 2 == 1:
                results.append(i)
    if not results:
        return []
    return results