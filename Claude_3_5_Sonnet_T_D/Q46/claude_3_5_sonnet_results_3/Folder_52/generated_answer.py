def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 75:
        return None
    num1, num2, num3 = (nums[19], nums[49], nums[74])
    return gcf(gcf(num1, num2), num3)