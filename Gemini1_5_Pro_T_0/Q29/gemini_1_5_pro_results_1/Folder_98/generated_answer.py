def gcf_two_nums(nums):
    i = nums[0]
    j = nums[9]
    while j:
        i, j = (j, i % j)
    return i