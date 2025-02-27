def even_ints_range_exclusive(nums):
    result = []
    for i in range(48, 77):
        if i % 2 == 0 and i in nums:
            result.append(i)
    return result