def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    return gcf(gcf(num1, num2), num3)