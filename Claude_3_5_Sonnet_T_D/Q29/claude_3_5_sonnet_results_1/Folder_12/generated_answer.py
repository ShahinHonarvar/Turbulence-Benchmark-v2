def gcf_two_nums(nums):
    a, b = (nums[56], nums[54])
    while b:
        a, b = (b, a % b)
    return a