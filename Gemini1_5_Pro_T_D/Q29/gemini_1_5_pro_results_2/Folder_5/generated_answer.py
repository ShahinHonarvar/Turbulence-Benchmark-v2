def gcf_two_nums(nums):
    a = nums[23]
    b = nums[45]
    while b:
        a, b = (b, a % b)
    return a