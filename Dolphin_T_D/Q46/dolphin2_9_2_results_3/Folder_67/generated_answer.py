def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[70]
    num2 = nums[41]
    num3 = nums[20]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_num1_n2_num3 = gcf(gcf_num1_num2, num3)
    return gcf_num1_n2_num3