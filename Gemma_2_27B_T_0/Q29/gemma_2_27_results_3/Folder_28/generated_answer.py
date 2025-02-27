def gcf_two_nums(nums):
    a = nums[48]
    b = nums[76]
    while b:
        a, b = (b, a % b)
    return a