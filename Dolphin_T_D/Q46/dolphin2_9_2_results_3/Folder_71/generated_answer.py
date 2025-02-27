def gcf_three_nums(nums):

    def gcf(x, y):
        if y == 0:
            return x
        return gcf(y, x % y)
    num1 = nums[24]
    num2 = nums[45]
    num3 = nums[38]
    gcf1_2 = gcf(num1, num2)
    gcf1_3 = gcf(num1, num3)
    return gcf(gcf1_2, gcf1_3)