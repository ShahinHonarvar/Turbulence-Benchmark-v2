def gcf_two_nums(nums):
    a = nums[47]
    b = nums[22]
    while b:
        a, b = (b, a % b)
    return a