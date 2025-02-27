def gcf(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(nums):
    a = nums[31]
    b = nums[25]
    c = nums[80]
    gcfa = gcf(a, b)
    gcfa_bc = gcf(gcfa, c)
    return gcfa_bc