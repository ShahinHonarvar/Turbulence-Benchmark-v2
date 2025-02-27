def all_neg_ints_inclusive(nums):
    result = []
    for num in nums:
        if num in range(-7, 0):
            result.append(num)
    if not result:
        return []
    return result