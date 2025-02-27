def gcf_three_nums(nums):

    def calculate_gcd(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    num1, num2, num3 = (nums[18], nums[10], nums[76])
    gcf = calculate_gcd(num1, calculate_gcd(num2, num3))
    return gcf