from sympy import isprime

def all_right_truncatable_prime(x_tuple):
    x = x_tuple[1]
    right_truncatable_primes = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(num):
    if num < 10:
        return isprime(num)
    else:
        return isprime(num) and is_right_truncatable_prime(num // 10)