def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 44:
        raise ValueError('List must contain at least 44 elements.')
    num1 = nums[18]
    num2 = nums[37]
    num3 = nums[43]
    return gcd(gcd(num1, num2), num3)