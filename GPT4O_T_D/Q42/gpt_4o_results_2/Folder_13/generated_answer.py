def prime_factors(nums):

    def get_prime_factors(n):
        factors = set()
        divisor = 2
        while n >= 2:
            while n % divisor == 0:
                factors.add(divisor)
                n //= divisor
            divisor += 1
        return factors
    if len(nums) > 126:
        return get_prime_factors(nums[126])
    return set()