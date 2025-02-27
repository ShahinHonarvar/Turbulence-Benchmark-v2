def all_odd_ints_exclusive(nums):
    result = []
    for i in range(len(nums)):
        if i < 2 and nums[i] % 2 != 0:
            result.append(nums[i])
    return result