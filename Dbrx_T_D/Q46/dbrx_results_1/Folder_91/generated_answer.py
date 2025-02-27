def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[8]
    num2 = nums[9]
    num3 = nums[3]
    return gcd(num1, gcd(num2, num3))