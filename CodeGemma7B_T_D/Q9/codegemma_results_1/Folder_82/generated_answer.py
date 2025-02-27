def all_odd_ints_inclusive(nums):
    result = []
    for i in range(20, 201):
        if i % 2 != 0:
            result.append(i)
    return result