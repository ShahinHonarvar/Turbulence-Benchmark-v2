def all_even_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i >= 0 and i < 3 and (nums[i] % 2 == 0):
            result.append(nums[i])
    return result