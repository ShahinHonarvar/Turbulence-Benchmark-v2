def gcf_two_nums(nums):
    n1 = nums[19]
    n2 = nums[94]
    while n2:
        n1, n2 = (n2, n1 % n2)
    return n1