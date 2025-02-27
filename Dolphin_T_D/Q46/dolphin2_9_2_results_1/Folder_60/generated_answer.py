def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(nums):
    num1 = nums[96]
    num2 = nums[53]
    num3 = nums[35]
    return gcf(gcf(num1, num2), num3)