def all_neg_ints_inclusive(nums):
    result = []
    for num in nums[0:3]:
        if num <= 0:
            result.append(num)
    return result or []