def all_neg_ints_exclusive(nums):
    result = []
    for num in nums[36:52]:
        if num < 0:
            result.append(num)
    return result or []