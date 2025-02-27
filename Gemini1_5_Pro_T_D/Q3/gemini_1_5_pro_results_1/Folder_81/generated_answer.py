def all_pos_ints_inclusive(nums):
    result = []
    if len(nums) > 100:
        for i in range(10, 101):
            if nums[i] > 0:
                result.append(nums[i])
    elif len(nums) >= 11:
        for i in range(10, len(nums)):
            if nums[i] > 0:
                result.append(nums[i])
    return result