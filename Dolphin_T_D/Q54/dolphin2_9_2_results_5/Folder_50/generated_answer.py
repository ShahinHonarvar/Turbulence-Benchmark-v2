def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[57]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = []
    for prime in primes:
        n = int(prime)
        while n != 0 and is_prime(n):
            right_truncatable_primes.append(n)
            n = int(str(n)[:-1])
    right_truncatable_primes = list(set(right_truncatable_primes))
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes