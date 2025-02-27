def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = set()
    for num in nums:
        if is_prime(num):
            primes.add(num)
    p_factors = set()
    for prime in primes:
        while nums[27] % prime == 0:
            p_factors.add(prime)
            nums[27] //= prime
    return p_factors