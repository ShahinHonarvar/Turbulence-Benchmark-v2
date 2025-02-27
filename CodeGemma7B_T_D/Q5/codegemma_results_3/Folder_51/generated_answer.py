def all_neg_ints_inclusive(nums):
    result = []
    for i in range(1, 9):
        if -i in nums:
            result.append(-i)
    return result