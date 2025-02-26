def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def multi_gcd(a, b, c):
        first_gcd = gcd(a, b)
        return gcd(first_gcd, c)
    return multi_gcd(nums[15], nums[51], nums[76])