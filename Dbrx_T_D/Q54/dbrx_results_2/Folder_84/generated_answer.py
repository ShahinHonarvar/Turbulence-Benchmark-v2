import itertools

def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = (False, False)
    for num in range(2, int(n ** 0.5) + 1):
        if primes[num]:
            primes[num * num:n + 1:num] = [False] * ((n - num * num) // num + 1)
    return [num for num in range(2, n + 1) if primes[num]]

def is_right_truncatable_prime(num):
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10
    return True

def is_prime(num):
    if num < 2:
        return False
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True

def all_right_truncatable_prime(n):
    primes = generate_primes(n)
    right_truncatable_primes = [num for num in primes if is_right_truncatable_prime(num)]
    return sorted(right_truncatable_primes, reverse=True)[:630]