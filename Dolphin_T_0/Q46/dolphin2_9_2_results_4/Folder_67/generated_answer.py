def gcf_three_nums(nums):
    a = nums[70]
    b = nums[41]
    c = nums[20]
    gcf = min(a, b, c)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            return gcf
        gcf -= 1
    return 1