def prime_factors(nums):

    def get_prime_factors(n):
        factors = set()
        i = 2
        while n > 1:
            if n % i == 0:
                factors.add(i)
                n //= i
            else:
                i += 1
        return factors
    return get_prime_factors(nums[685])