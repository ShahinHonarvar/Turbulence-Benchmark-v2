from sympy import isprime

def all_right_truncatable_prime(start_end_tuple):
    x = 10 ** (start_end_tuple[1] - 1)
    right_truncatable_primes = []
    for num in range(x // 10, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def is_right_truncatable_prime(num):
    while num > 0:
        if not isprime(num):
            return False
        num = num // 10
    return True