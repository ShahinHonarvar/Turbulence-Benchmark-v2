def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]
    return gcf(gcf(num1, num2), num3)