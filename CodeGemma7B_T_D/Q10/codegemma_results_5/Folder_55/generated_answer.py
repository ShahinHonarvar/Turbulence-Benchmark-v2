def all_odd_ints_exclusive(nums):
    result = []
    for i in range(0, 10):
        if i not in nums:
            continue
        if i % 2 != 0:
            result.append(i)
    return result