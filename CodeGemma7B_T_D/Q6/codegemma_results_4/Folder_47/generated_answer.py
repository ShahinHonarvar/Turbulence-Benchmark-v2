def all_neg_ints_exclusive(nums):
    result = []
    for num in nums[64:80]:
        if num < 0:
            result.append(num)
    return result