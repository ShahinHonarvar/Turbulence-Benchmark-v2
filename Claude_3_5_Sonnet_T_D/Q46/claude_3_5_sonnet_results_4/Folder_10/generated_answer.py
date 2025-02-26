def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[86]
    num2 = nums[89]
    num3 = nums[49]
    gcf_result = gcf(gcf(num1, num2), num3)
    return gcf_result