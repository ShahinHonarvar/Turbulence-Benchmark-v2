def all_left_right_truncatable_prime(x):
    primes = [i for i in range(x + 1) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    s = str(n)
    if '0' in s:
        return False
    for i in range(1, len(s)):
        left = int(s[:i])
        right = int(s[i:])
        if not (is_prime(left) and is_prime(right)):
            return False
    return True