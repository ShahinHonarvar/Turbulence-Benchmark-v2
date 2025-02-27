def gcf_three_nums(nums):
    num742 = nums[742]
    num888 = nums[888]
    num629 = nums[629]
    for i in range(min(num742, num888, num629), 0, -1):
        if num742 % i == 0 and num888 % i == 0 and (num629 % i == 0):
            return i