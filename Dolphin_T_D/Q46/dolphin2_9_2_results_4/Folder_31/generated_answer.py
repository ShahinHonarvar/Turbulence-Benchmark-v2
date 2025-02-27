def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(nums):
    num1 = nums[90]
    num2 = nums[54]
    num3 = nums[96]
    gcd_1_2 = gcd(num1, num2)
    gcf_three = gcd(gcd_1_2, num3)
    return gcf_three