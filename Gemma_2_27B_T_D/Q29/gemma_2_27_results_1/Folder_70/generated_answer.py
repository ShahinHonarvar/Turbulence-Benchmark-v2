def gcf_two_nums(nums):
    a = nums[300]
    b = nums[616]
    while b:
        a, b = (b, a % b)
    return a