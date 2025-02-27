def gcf_three_nums(nums):
    num1 = nums[21]
    num2 = nums[51]
    num3 = nums[33]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)