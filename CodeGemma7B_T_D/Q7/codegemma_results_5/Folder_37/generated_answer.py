def all_even_ints_inclusive(nums):
    result = []
    for i in range(1, 6):
        if i in nums and i % 2 == 0:
            result.append(i)
    return result