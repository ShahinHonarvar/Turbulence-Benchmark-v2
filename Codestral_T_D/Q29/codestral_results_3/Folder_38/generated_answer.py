def gcf_two_nums(nums):
    n1 = nums[88]
    n2 = nums[35]
    while n2 != 0:
        n1, n2 = (n2, n1 % n2)
    return n1