def gcf_two_nums(nums):
    i = nums[90]
    j = nums[84]
    while j:
        i, j = (j, i % j)
    return i