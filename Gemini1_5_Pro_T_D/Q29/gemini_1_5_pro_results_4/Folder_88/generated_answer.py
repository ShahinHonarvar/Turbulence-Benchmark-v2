def gcf_two_nums(nums):
    a = nums[27]
    b = nums[34]
    while b:
        a, b = (b, a % b)
    return a