def all_even_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(23, 24):
        if i < len(nums) and nums[i] % 2 == 0:
            result.append(nums[i])
    return result