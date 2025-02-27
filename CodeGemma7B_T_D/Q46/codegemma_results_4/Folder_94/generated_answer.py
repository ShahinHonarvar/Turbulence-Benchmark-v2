def gcf_three_nums(lst):
    nums = lst[56] * lst[88] * lst[51]
    factor = 2
    while factor <= nums:
        if nums % factor == 0:
            nums /= factor
        factor += 1
    return int(nums)