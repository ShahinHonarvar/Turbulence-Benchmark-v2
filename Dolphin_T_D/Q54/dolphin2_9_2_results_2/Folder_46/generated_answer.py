def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n, primes):
    if is_prime(n):
        for i in range(len(str(n)) - 1, 0, -1):
            if n // 10 ** i in primes:
                n = n % 10 ** i
            else:
                return False
    return True

def all_right_truncatable_prime(nums):
    primes = []
    x = nums[33]
    for i in range(x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        if is_right_truncatable_prime(prime, primes):
            right_truncatable_primes.append(prime)
    right_truncatable_primes.sort()
    return right_truncatable_primes