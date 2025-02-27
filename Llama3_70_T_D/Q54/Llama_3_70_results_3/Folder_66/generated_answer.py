def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p ** 2 <= n:
        if primes[p]:
            for i in range(p ** 2, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

def is_right_truncatable_prime(n, primes):
    num_str = str(n)
    for i in range(len(num_str)):
        if int(num_str[:len(num_str) - i]) not in primes:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[25]
    primes = sieve_of_eratosthenes(x)
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
    return sorted(right_truncatable_primes, reverse=True)