import functools
    import math

def gcf_three_nums(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    primes = [x for x in range(2, 10000) if is_prime(x)]

    def prime_factors(n):
        factors = []
        for prime in primes:
            if n % prime == 0:
                factors.append(prime)
                n //= prime
            if n == 1:
                break
        return factors
    nums = [nums[412], nums[932], nums[337]]
    factors = [prime_factors(num) for num in nums]
    common_factors = list(set(factors[0]).intersection(*factors[1:]))
    return functools.reduce(math.gcd, common_factors) if common_factors else 1