def gcf_two_nums(nums):
    a = nums[618]
    b = nums[195]
    while b:
        a, b = (b, a % b)
    return a