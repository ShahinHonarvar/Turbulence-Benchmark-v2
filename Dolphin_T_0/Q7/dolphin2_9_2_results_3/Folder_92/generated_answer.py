def all_even_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i <= 1:
            if nums[i] % 2 == 0:
                result.append(nums[i])
    return result