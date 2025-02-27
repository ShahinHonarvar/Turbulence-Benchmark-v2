def all_even_ints_exclusive(nums):
    result = []
    for i in range(10, 76):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result