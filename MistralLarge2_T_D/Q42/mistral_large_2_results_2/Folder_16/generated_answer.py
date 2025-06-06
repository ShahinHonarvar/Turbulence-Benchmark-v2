def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        return factors
    if len(nums) > 162:
        return factors(nums[162])
    return set()