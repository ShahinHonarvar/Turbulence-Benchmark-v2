def gcf_two_nums(nums):
    a = nums[166]
    b = nums[106]
    while b:
        a, b = (b, a % b)
    return a