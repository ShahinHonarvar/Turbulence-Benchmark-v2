def gcf_three_nums(nums):
    num1 = nums[34]
    num2 = nums[38]
    num3 = nums[77]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(num1, num2), num3)