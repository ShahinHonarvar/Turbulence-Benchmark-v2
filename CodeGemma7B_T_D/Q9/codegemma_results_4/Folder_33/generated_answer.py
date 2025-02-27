def all_odd_ints_inclusive(nums):
    result = []
    for i in range(667, 775):
        if i < len(nums) and nums[i] % 2 != 0:
            result.append(nums[i])
    return result