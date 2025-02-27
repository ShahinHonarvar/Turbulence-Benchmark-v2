from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def remove_digits(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return digits

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    digits = remove_digits(n)
    l = len(digits)
    for i in range(1, l):
        if not is_prime(int(''.join(map(str, digits[i:])))):
            return False
        if not is_prime(int(''.join(map(str, digits[:i])))):
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes) or []