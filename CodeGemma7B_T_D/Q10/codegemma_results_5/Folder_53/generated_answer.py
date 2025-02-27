def all_odd_ints_exclusive(nums):
    result = []
    for i in range(100, 101):
        if i in nums and i % 2 != 0:
            result.append(i)
    return result