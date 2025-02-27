def all_even_ints_exclusive(nums):
    results = []
    for i in range(29, 54):
        if nums[i] % 2 == 0 and i != 34:
            results.append(nums[i])
    return results