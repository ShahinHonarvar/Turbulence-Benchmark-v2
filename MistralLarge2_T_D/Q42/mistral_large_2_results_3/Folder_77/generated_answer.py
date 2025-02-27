def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, n + 1):
            while n % i == 0 and is_prime(i):
                factors.add(i)
                n //= i
        return factors
    if len(nums) > 985:
        return get_prime_factors(nums[985])
    else:
        return set()