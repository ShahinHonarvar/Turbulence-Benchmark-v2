def gcf_two_nums(nums):
    a = nums[3]
    b = nums[8]
    while b:
        a, b = (b, a % b)
    return a