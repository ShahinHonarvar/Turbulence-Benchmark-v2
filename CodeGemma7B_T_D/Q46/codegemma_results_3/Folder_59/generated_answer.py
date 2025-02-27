def gcf_three_nums(nums):
    return gcf(calc_lcm(nums[7], nums[6]), nums[8])

def calc_lcm(x, y):
    return abs(x * y) // gcf(x, y)

def gcf(x, y):
    return y if x % y == 0 else gcf(y, x % y)