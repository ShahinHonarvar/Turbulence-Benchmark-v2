def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors_of(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0:
                factors.add(i)
                n //= i
        return factors
    if len(nums) <= 49:
        return set()
    num = nums[49]
    return {f for f in factors_of(num) if is_prime(f)}