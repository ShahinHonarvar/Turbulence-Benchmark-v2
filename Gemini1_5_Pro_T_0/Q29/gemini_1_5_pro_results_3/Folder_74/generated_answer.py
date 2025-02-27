def gcf_two_nums(nums):
    a = nums[36]
    b = nums[85]
    while b:
        a, b = (b, a % b)
    return a