def all_even_ints_exclusive(nums):
    result = []
    for i in range(30, 200):
        if nums[i] % 2 == 0 and i != 30 and (i != 200):
            result.append(nums[i])
    return result