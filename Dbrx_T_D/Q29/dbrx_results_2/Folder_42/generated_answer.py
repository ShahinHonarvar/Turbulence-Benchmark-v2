def gcf_two_nums(nums):

    def gcd(a, b):
        return gcd(b, a % b) if b else a
    num1 = nums[84]
    num2 = nums[90]
    factor = gcd(num1, num2)
    return factor