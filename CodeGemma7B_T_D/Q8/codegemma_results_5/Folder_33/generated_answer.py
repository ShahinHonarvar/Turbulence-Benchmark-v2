def all_even_ints_exclusive(nums):
    result = []
    for i in range(369, 983):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    if not result:
        return []
    return result