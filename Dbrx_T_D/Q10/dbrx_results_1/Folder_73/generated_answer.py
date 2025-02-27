def all_odd_ints_exclusive(nums):
    result = []
    for i in range(36, 85):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            result.append(nums[i])
    return result