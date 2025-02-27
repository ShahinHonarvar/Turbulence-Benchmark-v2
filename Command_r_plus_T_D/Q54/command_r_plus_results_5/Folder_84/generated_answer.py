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
    x = numbers[630]
    primes = []
    for i in range(x):
        primes_list = right_truncatable_primes(i)
        primes.extend(primes_list)
    unique_primes = list(set(primes))
    sorted_primes = sorted(unique_primes, reverse=True)
    return sorted_primes