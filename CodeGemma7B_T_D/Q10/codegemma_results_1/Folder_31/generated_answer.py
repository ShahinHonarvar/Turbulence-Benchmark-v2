def all_odd_ints_exclusive(nums):
    odd_nums = []
    for i in range(87, 95):
        if i in nums:
            if i % 2 != 0:
                odd_nums.append(i)
    if not odd_nums:
        return []
    return odd_nums