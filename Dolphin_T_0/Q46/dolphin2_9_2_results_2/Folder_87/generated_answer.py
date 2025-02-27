def gcf_three_nums(nums):

    def gcd(num1, num2):
        while num2:
            num1, num2 = (num2, num1 % num2)
        return num1
    num1, num2, num3 = (nums[74], nums[60], nums[28])
    result = gcd(gcd(num1, num2), num3)
    return result