def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[20]
    num2 = nums[17]
    num3 = nums[28]
    result = gcf(gcf(num1, num2), num3)
    return result