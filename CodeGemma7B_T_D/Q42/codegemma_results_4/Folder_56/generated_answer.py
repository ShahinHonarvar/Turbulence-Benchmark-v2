def prime_factors(nums):
    prime_factors = set()
    for factor in nums:
        if factor % nums[60] == 0:
            primes = get_primes(factor)
            prime_factors.update(primes)
    return prime_factors

def get_primes(n):
    primes = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                primes.add(i)
                n //= i
    return primes