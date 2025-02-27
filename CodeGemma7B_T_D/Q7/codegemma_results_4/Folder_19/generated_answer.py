def all_even_ints_inclusive(nums):
    result = []
    for i in range(3, 6):
        if i < len(nums) and nums[i] % 2 == 0:
            result.append(nums[i])
    if not result:
        return []
    return result