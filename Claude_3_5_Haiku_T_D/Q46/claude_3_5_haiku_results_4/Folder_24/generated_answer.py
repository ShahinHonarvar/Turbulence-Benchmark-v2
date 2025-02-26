def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]
    current_gcf = gcd(num1, num2)
    current_gcf = gcd(current_gcf, num3)
    return current_gcf