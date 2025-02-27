def gcf_three_nums(nums):
    a = nums[18]
    b = nums[10]
    c = nums[76]
    gcf = min(a, b, c)
    while gcf > 0:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            break
        gcf -= 1
    return gcf