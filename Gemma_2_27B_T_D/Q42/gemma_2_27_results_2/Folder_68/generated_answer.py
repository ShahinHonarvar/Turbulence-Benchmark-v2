def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    n = nums[3]
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            if is_prime(i):
                factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors