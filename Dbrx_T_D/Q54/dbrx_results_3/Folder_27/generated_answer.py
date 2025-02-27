from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[79]
    right_truncatable_primes = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(n):
    if n < 10:
        return isprime(n)
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[:-1])
    return True