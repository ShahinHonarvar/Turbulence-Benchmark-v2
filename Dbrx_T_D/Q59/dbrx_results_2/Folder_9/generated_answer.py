def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    primes = [i for i in range(1, x) if is_prime(i)]
    left_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        if all((is_prime(int(s[i:])) for i in range(1, len(s)))):
            left_truncatable_primes.append(prime)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes