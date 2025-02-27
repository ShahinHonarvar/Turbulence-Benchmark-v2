from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    result = []
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(n):
    if not (1 < n < 10 and isprime(n)):
        return False
    while n > 9:
        n = n % 10
        if not isprime(n):
            return False
    return True