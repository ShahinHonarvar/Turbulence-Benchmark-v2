def gcf_three_nums(nums):
    num1 = nums[7]
    num2 = nums[3]
    num3 = nums[7]
    return gcf(num1, gcf(num2, num3))

def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)