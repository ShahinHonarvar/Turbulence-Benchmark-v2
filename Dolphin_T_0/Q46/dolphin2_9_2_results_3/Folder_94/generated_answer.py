def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[88]
    num3 = lst[51]
    nums = [num1, num2, num3]
    gcf = nums[0]
    for i in range(1, len(nums)):
        gcf = gcd(gcf, nums[i])
    return gcf