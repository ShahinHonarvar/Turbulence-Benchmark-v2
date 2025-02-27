def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, IntEnum() + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
        return factors
    return prime_factors_of(nums[13])