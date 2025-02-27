def gcf_three_nums(nums):
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(num1, gcf(num2, num3))