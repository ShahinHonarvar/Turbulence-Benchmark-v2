def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        d = 2
        while n > 1:
            while n % d == 0:
                if is_prime(d):
                    factors_set.add(d)
                n //= d
            d += 1
        return factors_set
    if len(nums) > 29:
        return factors(nums[29])
    else:
        return set()