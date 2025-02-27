def all_odd_ints_exclusive(nums):
    result = []
    for i in range(1, 8):
        if i % 2 != 0 and i in nums:
            result.append(i)
    return result