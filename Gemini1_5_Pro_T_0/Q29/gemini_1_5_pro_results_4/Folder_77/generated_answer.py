def gcf_two_nums(nums):
    a = nums[841]
    b = nums[804]
    while b:
        a, b = (b, a % b)
    return a