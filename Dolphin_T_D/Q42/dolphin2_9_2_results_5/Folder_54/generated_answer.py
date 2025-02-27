def prime_factors(nums):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
                if i != n // i and is_prime(n // i):
                    factors.add(n // i)
        return factors
    return prime_factors_of(nums[51])