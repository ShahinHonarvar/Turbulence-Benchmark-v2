def prime_factors(nums):
    primes = set()
    prime = 2
    while nums[632] != 1:
        while nums[632] % prime == 0:
            primes.add(prime)
            nums[632] //= prime
        prime += 1
    return primes