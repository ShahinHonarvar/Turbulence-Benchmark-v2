def gcf_two_nums(nums):
    i = nums[33]
    j = nums[72]
    while j:
        i, j = (j, i % j)
    return i