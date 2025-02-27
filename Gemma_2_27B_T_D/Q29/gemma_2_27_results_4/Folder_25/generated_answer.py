def gcf_two_nums(nums):
    a = nums[41]
    b = nums[69]
    while b:
        a, b = (b, a % b)
    return a