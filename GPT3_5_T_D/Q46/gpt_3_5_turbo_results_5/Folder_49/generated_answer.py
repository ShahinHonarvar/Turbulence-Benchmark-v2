def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = nums[34]
    num2 = nums[38]
    num3 = nums[77]
    gcd1 = gcd(num1, num2)
    gcf = gcd(gcd1, num3)
    return gcf