from sympy import isprime

def all_left_right_truncatable_prime(arg):
    left_right_truncatable_primes = []
    x = arg[100]
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable(num):
    while num > 0:
        if not is_prime(num):
            return False
        num = num // 10 if num >= 10 else 0
    return True