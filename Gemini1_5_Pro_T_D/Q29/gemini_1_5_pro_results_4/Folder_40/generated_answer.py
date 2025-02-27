def gcf_two_nums(nums):
    i = nums[7]
    j = nums[9]
    while j:
        i, j = (j, i % j)
    return i