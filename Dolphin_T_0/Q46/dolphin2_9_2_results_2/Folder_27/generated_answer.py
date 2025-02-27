def gcf_three_nums(nums):
    a, b, c = (nums[76], nums[64], nums[28])
    gcf = min(a, b, c)
    while True:
        if a % gcf == 0 and b % gcf == 0 and (c % gcf == 0):
            return gcf
        else:
            gcf -= 1