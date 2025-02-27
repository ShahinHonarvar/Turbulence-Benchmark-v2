def gcf_three_nums(nums):
    num1 = nums[145]
    num2 = nums[183]
    num3 = nums[770]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)