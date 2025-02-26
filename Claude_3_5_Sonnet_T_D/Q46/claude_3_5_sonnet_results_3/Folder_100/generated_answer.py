def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[21]
    num2 = nums[51]
    num3 = nums[33]
    return gcf(gcf(num1, num2), num3)