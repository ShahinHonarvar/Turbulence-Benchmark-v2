def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[18]
    num2 = nums[48]
    num3 = nums[73]
    return gcd(gcd(num1, num2), num3)