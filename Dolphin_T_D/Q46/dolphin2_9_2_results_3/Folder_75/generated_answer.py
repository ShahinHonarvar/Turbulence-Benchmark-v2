def gcf_three_nums(nums):
    num1 = nums[70]
    num2 = nums[98]
    num3 = nums[22]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result