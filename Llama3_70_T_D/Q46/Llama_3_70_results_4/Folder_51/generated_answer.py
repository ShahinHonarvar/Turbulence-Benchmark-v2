def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[21]
    num2 = nums[69]
    num3 = nums[41]
    gcf_num1_num2 = gcf(num1, num2)
    return gcf(gcf_num1_num2, num3)