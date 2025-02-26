def prime_factors(nums):

    def factors(n):
        f = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                f.add(d)
                n //= d
            d += 1
        if n > 1:
            f.add(n)
        return f
    return factors(nums[64])