def all_even_ints_exclusive(nums):
    result = []
    for i in range(1, 2):
        if nums[i] % 2 == 0 and i > 0 and (i < len(nums) - 1):
            result.append(nums[i])
    return result