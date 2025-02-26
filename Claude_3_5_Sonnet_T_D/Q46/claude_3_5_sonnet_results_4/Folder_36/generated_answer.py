def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[427]
    num2 = nums[761]
    num3 = nums[148]
    return gcf(gcf(num1, num2), num3)