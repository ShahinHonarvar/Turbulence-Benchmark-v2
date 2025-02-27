def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[8]
    num2 = nums[2]
    num3 = nums[1]
    gcf_1_2 = gcf(num1, num2)
    return gcf(gcf_1_2, num3)