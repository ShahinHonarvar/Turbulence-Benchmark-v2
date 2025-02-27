def all_even_ints_exclusive(nums):
    if not nums or 56 >= len(nums) or len(nums) - 1 <= 88:
        return []
    result = []
    for i in range(56, 88):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result