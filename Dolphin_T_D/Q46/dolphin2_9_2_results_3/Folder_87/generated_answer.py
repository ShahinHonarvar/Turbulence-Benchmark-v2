def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[74]
    num2 = nums[60]
    num3 = nums[28]
    gcf_value = gcf(gcf(num1, num2), num3)
    return gcf_value