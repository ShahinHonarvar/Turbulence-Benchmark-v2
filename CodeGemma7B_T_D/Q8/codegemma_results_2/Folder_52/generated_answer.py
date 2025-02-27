def all_even_ints_exclusive(nums):
    result = []
    for i in range(93, 94):
        if nums[i] % 2 == 0 and i != 93:
            result.append(nums[i])
    return result