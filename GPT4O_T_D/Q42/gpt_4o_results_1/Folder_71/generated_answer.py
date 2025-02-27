def prime_factors(nums):

    def find_prime_factors(n):
        factors = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    if len(nums) <= 78:
        return set()
    return find_prime_factors(nums[78])