def all_even_ints_exclusive(nums):
    if not nums:
        return []
    ret = []
    for i in range(51, 76):
        if nums[i] % 2 == 0 and i != 51:
            ret.append(nums[i])
    return ret or []