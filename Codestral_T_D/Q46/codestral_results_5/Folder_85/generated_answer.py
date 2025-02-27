def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[49]
    num2 = nums[46]
    num3 = nums[13]
    return gcf(gcf(num1, num2), num3)