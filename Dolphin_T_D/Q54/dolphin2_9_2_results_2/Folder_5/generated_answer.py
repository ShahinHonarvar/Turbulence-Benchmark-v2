from sympy import isprime

def is_right_truncatable_prime(n):
    if isprime(n):
        while n > 9:
            if not isprime(n // 10):
                return False
            n //= 10
        return True
    return False

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            primes.append(n)
    return sorted(primes)