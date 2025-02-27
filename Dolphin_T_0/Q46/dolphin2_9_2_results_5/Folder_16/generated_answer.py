def gcf_three_nums(nums):
    num1 = nums[558]
    num2 = nums[110]
    num3 = nums[628]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(num1, num2), num3)