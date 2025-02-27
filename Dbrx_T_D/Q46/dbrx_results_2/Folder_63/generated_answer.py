def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[38]
    num2 = nums[52]
    num3 = nums[69]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf