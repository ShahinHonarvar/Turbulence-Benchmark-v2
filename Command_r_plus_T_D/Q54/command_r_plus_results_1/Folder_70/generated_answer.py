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

def right_truncatable_primes(n):
    primes = []
    for i in range(n, 0, -1):
        if str(i) in str(n) and is_prime(i):
            primes.append(i)
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[433]
    primes = []
    for i in range(x):
        primes_list = right_truncatable_primes(i)
        primes.extend(primes_list)
    return sorted(set(primes), reverse=True)