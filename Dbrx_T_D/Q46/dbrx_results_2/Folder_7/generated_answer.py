def gcf_three_nums(nums):

    def gcf(num1, num2):
        while num1 % num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num2
    a, b, c = (nums[477], nums[696], nums[663])
    return gcf(gcf(a, b), c)