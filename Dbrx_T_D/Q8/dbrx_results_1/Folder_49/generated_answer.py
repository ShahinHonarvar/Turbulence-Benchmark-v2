def all_even_ints_exclusive(nums):
    if len(nums) < 200:
        return []
    result = []
    for i in range(80, 200):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result