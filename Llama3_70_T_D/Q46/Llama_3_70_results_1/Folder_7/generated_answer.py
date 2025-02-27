def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[477]
    num2 = nums[696]
    num3 = nums[663]
    return gcd(gcd(num1, num2), num3)