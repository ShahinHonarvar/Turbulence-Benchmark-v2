def all_even_ints_inclusive(nums):
    result = []
    for i in range(56, 82):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result