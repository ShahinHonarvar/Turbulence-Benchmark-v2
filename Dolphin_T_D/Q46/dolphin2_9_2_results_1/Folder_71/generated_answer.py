def gcf_three_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    num1 = nums[24]
    num2 = nums[45]
    num3 = nums[38]
    return gcd(gcd(num1, num2), num3)