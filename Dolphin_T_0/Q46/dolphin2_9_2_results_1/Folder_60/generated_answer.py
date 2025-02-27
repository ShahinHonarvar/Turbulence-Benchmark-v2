def gcf_three_nums(lst):
    nums = [lst[96], lst[53], lst[35]]
    n1, n2 = (nums[0], nums[1])
    while n1 != n2:
        if n1 > n2:
            n1 -= n2
        else:
            n2 -= n1
    n3 = nums[2]
    while n3 != 0:
        n1, n2 = (n2, n1 % n2)
        n3 = n3 % n1
    gcf = n1
    return gcf