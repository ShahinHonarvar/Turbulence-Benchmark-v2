def all_neg_ints_exclusive(nums):
    result = []
    for num in nums:
        if num < 0 and nums.index(num) < 6 and (nums.index(num) > 0):
            result.append(num)
    return result