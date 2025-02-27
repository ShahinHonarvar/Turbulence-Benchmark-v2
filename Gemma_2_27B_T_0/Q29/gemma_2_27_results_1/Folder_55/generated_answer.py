def gcf_two_nums(nums):
    a = nums[2]
    b = nums[1]
    while b:
        a, b = (b, a % b)
    return a