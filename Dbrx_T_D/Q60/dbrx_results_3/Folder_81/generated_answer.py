from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[98]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes)

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while len(str(num)) > 1:
        num = int(str(num)[1:])
        if not isprime(num):
            return False
        num = int(str(num)[:-1])
    return isprime(num)