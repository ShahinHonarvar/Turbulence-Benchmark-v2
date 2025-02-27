def all_neg_ints_exclusive(nums):
    result = []
    for num in nums:
        if num < 0:
            if len(result) == 0 or num >= result[-1]:
                result.append(num)
    return result