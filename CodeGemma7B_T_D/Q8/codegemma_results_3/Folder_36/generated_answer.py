def all_even_ints_exclusive(nums):
    res = []
    for i in nums[598:767]:
        if i % 2 == 0 and i != 0:
            res.append(i)
    if not res:
        return []
    return res