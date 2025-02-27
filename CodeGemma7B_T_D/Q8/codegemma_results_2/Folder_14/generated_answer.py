def all_even_ints_exclusive(nums):
    result = []
    for i in range(1, 8):
        if i % 2 == 0 and nums[i] % 2 == 0 and (i != 7):
            result.append(nums[i])
    return result