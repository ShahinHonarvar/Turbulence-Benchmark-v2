def all_even_ints_exclusive(nums):
    if len(nums) < 77:
        return []
    result = []
    for i in range(51, 76):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result