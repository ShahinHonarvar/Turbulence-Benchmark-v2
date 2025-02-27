def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[252]
    num2 = nums[149]
    num3 = nums[564]
    gcf_num1_num2 = gcf(num1, num2)
    greatest_common_factor = gcf(gcf_num1_num2, num3)
    return greatest_common_factor