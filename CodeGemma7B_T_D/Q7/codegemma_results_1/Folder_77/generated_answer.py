def all_even_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for i in range(527, 539):
        if i >= 0 and i < len(nums) and (nums[i] % 2 == 0):
            result.append(nums[i])
    if not result:
        return []
    return result