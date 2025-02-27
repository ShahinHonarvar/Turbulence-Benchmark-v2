def gcf_two_nums(nums):
    a = nums[534]
    b = nums[630]
    while b:
        a, b = (b, a % b)
    return a