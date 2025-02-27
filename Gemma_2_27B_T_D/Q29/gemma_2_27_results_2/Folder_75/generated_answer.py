def gcf_two_nums(nums):
    a = nums[42]
    b = nums[25]
    while b:
        a, b = (b, a % b)
    return a