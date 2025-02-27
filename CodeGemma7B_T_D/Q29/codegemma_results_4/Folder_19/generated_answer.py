def gcf_two_nums(nums):
    n1, n2 = (nums[66], nums[90])
    common_factor = 1
    while n2 != 0:
        n1, n2 = (n2, n1 % n2)
    return n1