def gcf_two_nums(nums):
    a = nums[894]
    b = nums[801]
    while b:
        a, b = (b, a % b)
    return a