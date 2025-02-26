def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 54:
        return None
    num1, num2, num3 = (nums[29], nums[42], nums[53])
    return gcf(gcf(num1, num2), num3)