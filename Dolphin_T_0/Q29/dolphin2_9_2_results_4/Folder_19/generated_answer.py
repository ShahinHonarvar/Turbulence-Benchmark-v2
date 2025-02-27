def gcf_two_nums(nums):
    a = nums[66]
    b = nums[90]
    gcf = min(a, b)
    while gcf > 1:
        if a % gcf == 0 and b % gcf == 0:
            return gcf
        gcf -= 1
    return 1