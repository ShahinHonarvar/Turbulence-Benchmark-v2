def gcf_two_nums(nums):
    n1 = nums[15]
    n2 = nums[99]
    while n2:
        n1, n2 = (n2, n1 % n2)
    return n1