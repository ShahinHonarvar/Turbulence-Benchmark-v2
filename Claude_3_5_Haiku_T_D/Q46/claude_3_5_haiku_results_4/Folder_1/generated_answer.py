def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcd_multiple(a, b, c):
        first_gcd = gcd(a, b)
        return gcd(first_gcd, c)
    return gcd_multiple(nums[74], nums[51], nums[27])