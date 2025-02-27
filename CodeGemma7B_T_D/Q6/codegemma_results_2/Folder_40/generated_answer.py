def all_neg_ints_exclusive(nums):
    result = []
    for num in nums:
        if -3 < num < 0:
            result.append(num)
    return result