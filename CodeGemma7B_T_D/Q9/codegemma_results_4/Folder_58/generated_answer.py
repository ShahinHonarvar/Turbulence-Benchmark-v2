def all_odd_ints_inclusive(nums):
    result = []
    for i in range(209, 557):
        if i % 2 != 0:
            result.append(i)
    return result