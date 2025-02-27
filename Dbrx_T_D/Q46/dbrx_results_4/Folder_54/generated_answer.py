def gcf_three_nums(nums):
    a = nums[96]
    b = nums[57]
    c = nums[85]

    def gcd(m, n):
        while n != 0:
            m, n = (n, m % n)
        return m

    def lcm(m, n):
        return m * n // gcd(m, n)
    return gcd(lcm(a, b), c)