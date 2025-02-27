def all_odd_ints_inclusive(nums):
    result = []
    for i in range(310, 371):
        if i >= 0 and i < len(nums) and (nums[i] % 2 != 0):
            result.append(nums[i])
    return result