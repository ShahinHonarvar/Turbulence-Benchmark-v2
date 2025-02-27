import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:])
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True

def all_left_right_truncatable_prime(high_range):
    x = 10 ** 15
    primes = [i for i in range(2, high_range + 1) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if is_left_truncatable(i)]
    right_truncatable_primes = [i for i in primes if is_right_truncatable(i)]
    lr_truncatable_primes = [i for i in left_truncatable_primes if i in right_truncatable_primes]
    return sorted(lr_truncatable_primes, reverse=True)