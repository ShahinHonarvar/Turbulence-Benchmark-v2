def gcf_three_nums(nums):
    num1 = nums[427]
    num2 = nums[761]
    num3 = nums[148]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    return gcf(gcf(num1, num2), num3)