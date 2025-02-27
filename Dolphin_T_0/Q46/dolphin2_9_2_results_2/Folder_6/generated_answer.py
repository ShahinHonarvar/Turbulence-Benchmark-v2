def gcf_three_nums(nums):
    num1 = nums[93]
    num2 = nums[94]
    num3 = nums[57]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    result = gcf(min(num1, num2, num3), gcf(max(num1, num2, num3), gcf(num1, num2, num3)))
    return result