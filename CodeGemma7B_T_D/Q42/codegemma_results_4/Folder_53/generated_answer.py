def prime_factors(nums):
    primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    result = set()
    num = nums[73]
    for prime in primes:
        while num % prime == 0:
            result.add(prime)
            num //= prime
    return result