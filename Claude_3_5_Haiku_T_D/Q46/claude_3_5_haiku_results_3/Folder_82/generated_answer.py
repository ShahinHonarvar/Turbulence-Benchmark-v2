def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[67], nums[84], nums[13])
    first_gcd = gcd(a, b)
    return gcd(first_gcd, c)