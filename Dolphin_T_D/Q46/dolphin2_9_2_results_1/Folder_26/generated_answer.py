def gcf_three_nums(nums):

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    num1 = nums[15]
    num2 = nums[51]
    num3 = nums[76]
    return gcf(gcf(num1, num2), num3)