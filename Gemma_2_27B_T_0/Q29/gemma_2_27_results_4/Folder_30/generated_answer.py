def gcf_two_nums(nums):
    a = nums[85]
    b = nums[33]
    while b:
        a, b = (b, a % b)
    return a