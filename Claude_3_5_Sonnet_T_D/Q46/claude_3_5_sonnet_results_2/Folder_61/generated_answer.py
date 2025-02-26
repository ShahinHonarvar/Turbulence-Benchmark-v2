def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 8:
        return None
    num1, num2, num3 = (nums[1], nums[2], nums[7])
    return gcf(gcf(num1, num2), num3)