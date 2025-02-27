def all_neg_ints_exclusive(nums):
    result = []
    for num in nums:
        if num < 0 and num < 100 and (num > 10):
            result.append(num)
    return result