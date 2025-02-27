def gcf_three_nums(nums):
    num1 = nums[17]
    num2 = nums[88]
    num3 = nums[35]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    gcf_num1_num2 = gcf(num1, num2)
    result = gcf(gcf_num1_num2, num3)
    return result