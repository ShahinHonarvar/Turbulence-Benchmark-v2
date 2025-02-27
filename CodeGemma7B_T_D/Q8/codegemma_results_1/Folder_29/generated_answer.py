def all_even_ints_exclusive(nums):
    result = []
    for i in range(48, 77):
        if i % 2 == 0 and i in nums:
            result.append(i)
    return result