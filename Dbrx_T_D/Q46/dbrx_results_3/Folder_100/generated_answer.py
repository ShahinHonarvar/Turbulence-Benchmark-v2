def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    num1, num2, num3 = (nums[21], nums[51], nums[33])
    return lcm(num1, num2) // gcd(num1, num3)