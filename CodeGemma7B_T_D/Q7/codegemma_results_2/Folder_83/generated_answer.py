def all_even_ints_inclusive(nums):
    result = []
    for i in range(90, 201):
        if i in range(len(nums)) and nums[i] % 2 == 0:
            result.append(nums[i])
    return result