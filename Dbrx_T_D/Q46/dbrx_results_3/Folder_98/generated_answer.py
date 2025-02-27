def gcf_three_nums(nums):

    def calculate_gcf(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    return calculate_gcf(nums[8], calculate_gcf(nums[2], nums[1]))