def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[693], nums[331], nums[668])
    factor_a_b = gcd(a, b)
    return gcd(factor_a_b, c)