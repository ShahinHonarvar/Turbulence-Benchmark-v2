def all_neg_ints_inclusive(nums):
    result = []
    if len(nums) > 6:
        for i in range(6, 7):
            if nums[i] < 0:
                result.append(nums[i])
        return result
    else:
        return result