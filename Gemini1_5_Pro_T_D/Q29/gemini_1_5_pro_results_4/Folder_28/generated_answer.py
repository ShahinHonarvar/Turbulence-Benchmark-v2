def gcf_two_nums(nums):
    i = nums[48]
    j = nums[76]
    while j:
        i, j = (j, i % j)
    return i