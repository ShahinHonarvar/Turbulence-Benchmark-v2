def gcf(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(list_nums):
    num1, num2, num3 = (list_nums[99], list_nums[28], list_nums[53])
    gcd = gcf(num1, num2)
    gcd = gcf(gcd, num3)
    return gcd