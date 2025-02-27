def all_neg_ints_exclusive(nums):
    negative_ints = []
    for num in nums:
        if num < 0 and num not in range(10):
            negative_ints.append(num)
    return negative_ints