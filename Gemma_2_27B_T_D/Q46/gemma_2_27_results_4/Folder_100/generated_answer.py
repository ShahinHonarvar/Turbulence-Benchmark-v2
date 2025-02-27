def gcf_three_nums(nums):
    a = nums[21]
    b = nums[51]
    c = nums[33]
    while a:
        a, b = (b % a, a)
    return b