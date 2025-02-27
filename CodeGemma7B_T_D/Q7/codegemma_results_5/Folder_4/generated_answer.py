def all_even_ints_inclusive(nums):
    result = []
    for i in range(12, 93):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result if len(result) != 0 else []