def gcf_three_nums(nums):
    n1, n2, n3 = (nums[16], nums[87], nums[95])
    x = n1
    while x > 0:
        if n2 % x == 0 and n3 % x == 0:
            return x
        x -= 1
    return 1