def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[637]
    num2 = nums[411]
    num3 = nums[757]
    return gcf(gcf(num1, num2), num3)