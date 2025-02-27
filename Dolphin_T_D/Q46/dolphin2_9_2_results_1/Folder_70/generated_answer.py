def gcf_three_nums(nums):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    num1 = nums[990]
    num2 = nums[671]
    num3 = nums[711]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_num1_num2_num3 = gcf(gcf_num1_num2, num3)
    return gcf_num1_num2_num3