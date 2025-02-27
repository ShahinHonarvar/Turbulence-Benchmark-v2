def all_neg_ints_inclusive(nums):
    lis = []
    for num in nums[62:93]:
        if num < 0:
            lis.append(num)
    if lis == []:
        return []
    return lis