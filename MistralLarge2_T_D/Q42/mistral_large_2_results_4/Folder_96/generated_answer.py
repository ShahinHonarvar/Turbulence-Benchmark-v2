def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors_set.add(d)
                n //= d
            else:
                d += 1
        if n > 1:
            factors_set.add(n)
        return factors_set
    num = nums[47]
    prime_factors_set = set(filter(is_prime, factors(num)))
    return prime_factors_set