def all_left_right_truncatable_prime(t):
    x = t[645]
    primes = [prime for prime in range(x + 1) if isprime(prime) and (not str(prime).startswith('0'))]
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_prime = str(n)
    for i in range(1, len(str_prime)):
        left = int(str_prime[:i])
        right = int(str_prime[i:])
        if not (isprime(left) and isprime(right)):
            return False
    return True