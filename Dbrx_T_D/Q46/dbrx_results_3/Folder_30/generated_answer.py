def gcf_three_nums(nums):
    num1, num2, num3 = (nums[76], nums[35], nums[74])

    def calculate_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf1 = calculate_gcf(num1, num2)
    gcf2 = calculate_gcf(gcf1, num3)
    return gcf2