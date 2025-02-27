from sympy import isprime

def all_right_truncatable_prime(n):
    result = []
    for num in range(1, n):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_right_truncatable_prime(num):
    while num > 0:
        if not isprime(num):
            return False
        num //= 10
    return True