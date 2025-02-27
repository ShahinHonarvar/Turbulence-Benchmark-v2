def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (nums[32], nums[54], nums[13])
    return gcf(gcf(num1, num2), num3)