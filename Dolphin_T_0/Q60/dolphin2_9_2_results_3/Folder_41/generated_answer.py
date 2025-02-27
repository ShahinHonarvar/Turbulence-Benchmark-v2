def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_truncatable(n):
    num = n
    while num > 0:
        if num % 10 == 0:
            return False
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_right_truncatable_prime(input):
    x = input[46]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes if primes else []