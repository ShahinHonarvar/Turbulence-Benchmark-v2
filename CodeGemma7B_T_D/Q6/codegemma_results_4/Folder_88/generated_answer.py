def all_neg_ints_exclusive(nums):
    result = []
    for num in nums[2:8]:
        if num < 0:
            result.append(num)
    return result