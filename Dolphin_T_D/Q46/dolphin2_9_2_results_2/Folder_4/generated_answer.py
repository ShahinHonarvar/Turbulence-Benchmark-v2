def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(nums):
    num1 = nums[24]
    num2 = nums[25]
    num3 = nums[80]
    gcf_nums = gcf(gcf(num1, num2), num3)
    return gcf_nums