def gcf_two_nums(nums):
    a = nums[872]
    b = nums[219]
    while b:
        a, b = (b, a % b)
    return a