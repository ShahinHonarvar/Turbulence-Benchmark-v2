import sympy

def is_prune(n):
    return sympy.isprime(n)

def is_left_truncatable(n):
    if n < 10:
        return True
    else:
        return is_prune(n) and is_left_truncatable(n // 10)

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[88]
    primes = [i for i in range(2, x) if is_prune(i) and is_left_truncatable(i)]
    primes.sort()
    return primes