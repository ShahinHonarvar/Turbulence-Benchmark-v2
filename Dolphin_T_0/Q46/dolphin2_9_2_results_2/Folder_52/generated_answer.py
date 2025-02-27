def gcf(n, d):
    while d != 0:
        t = d
        d = n % d
        n = t
    return n

def gcf_three_nums(nums):
    return gcf(gcf(nums[19], nums[49]), nums[74])