def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(prime, primes_set):
    while prime > 0:
        if is_prime(prime) and prime in primes_set:
            prime = int(str(prime)[-1])
        else:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[41]
    primes_set = {i for i in range(2, x) if is_prime(i)}
    return sorted([i for i in primes_set if is_right_truncatable_prime(i, primes_set)])