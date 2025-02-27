def all_left_truncatable_prime(x):
    primes = [p for p in range(x) if is_prime(p) and str(p) not in '0']
    result = []
    for prime in primes:
        if is_left_truncatable_prime(prime):
            result.append(prime)
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(prime):
    str_prime = str(prime)
    for i in range(1, len(str_prime)):
        if not is_prime(int(str_prime[i:])):
            return False
    return True