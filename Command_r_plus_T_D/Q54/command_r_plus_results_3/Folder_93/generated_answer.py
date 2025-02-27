def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(num):
    primes = []
    while num > 0:
        if is_prime(num):
            primes.append(num)
        num //= 10
    return primes

def all_right_truncatable_prime(numbers):
    x = numbers[11]
    truncatable_primes = []
    for num in range(2, x):
        primes = right_truncatable_primes(num)
        if primes and primes[-1] < x:
            truncatable_primes.extend(primes)
    return sorted(truncatable_primes)