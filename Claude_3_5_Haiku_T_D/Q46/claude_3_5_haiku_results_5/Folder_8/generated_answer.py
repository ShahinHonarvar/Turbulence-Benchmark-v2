def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[99], nums[28], nums[53])
    first_two_gcd = gcd(a, b)
    return gcd(first_two_gcd, c)