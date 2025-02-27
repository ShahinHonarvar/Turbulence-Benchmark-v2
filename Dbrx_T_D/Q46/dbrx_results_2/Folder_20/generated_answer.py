def gcf_three_nums(nums):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    num1 = nums[29]
    num2 = nums[53]
    num3 = nums[42]
    return gcd(num1, gcd(num2, num3))