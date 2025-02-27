from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[28]
    result = []
    for num in range(1, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result) if result else []

def is_left_right_truncatable_prime(n):
    if n < 0 or '0' in str(n):
        return False
    while n > 9 and isprime(n):
        n //= 10
    while n > 9 and is_left_truncatable_prime(n):
        n //= 10
    return isprime(n)

def is_left_truncatable_prime(n):
    while n > 0 and isprime(n):
        n //= 10
    return n == 0