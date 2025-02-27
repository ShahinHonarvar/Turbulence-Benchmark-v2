def gcf_three_nums(nums):
    a = nums[22]
    b = nums[97]
    c = nums[64]

    def gcd(m, n):
        while n:
            m, n = (n, m % n)
        return m

    def lcm(m, n):
        return m * n // gcd(m, n)
    return gcd(gcd(a, b), c)