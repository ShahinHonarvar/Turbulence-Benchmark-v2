def gcf_three_nums(nums):
    num695 = nums[695]
    num710 = nums[710]
    num914 = nums[914]
    gcf = min(num695, num710, num914)
    while True:
        if num695 % gcf == 0 and num710 % gcf == 0 and (num914 % gcf == 0):
            return gcf
        gcf -= 1