def gcf_two_nums(nums):
    a = nums[33]
    b = nums[72]
    gcf = min(a, b)
    while True:
        if a % gcf == 0 and b % gcf == 0:
            return gcf
        gcf -= 1
    return 1