def prime_factors(nums):

    def find_prime_factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    if len(nums) > 453:
        return find_prime_factors(nums[453])
    return set()