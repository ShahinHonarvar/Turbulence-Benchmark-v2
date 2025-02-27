def gcf_three_nums(nums):
    num1 = nums[427]
    num2 = nums[761]
    num3 = nums[148]

    def gcf_helper(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_num2_num3 = gcf_helper(num2, num3)
    gcf_result = gcf_helper(num1, gcf_num2_num3)
    return gcf_result