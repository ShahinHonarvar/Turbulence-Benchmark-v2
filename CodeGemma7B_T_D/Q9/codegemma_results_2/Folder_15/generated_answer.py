def all_odd_ints_inclusive(nums):
    result = []
    for i in range(4):
        if i >= len(nums) or nums[i] % 2 != 0:
            result.append(nums[i])
    return result