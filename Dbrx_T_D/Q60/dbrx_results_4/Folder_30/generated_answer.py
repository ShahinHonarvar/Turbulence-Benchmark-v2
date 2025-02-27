from sympy import isprime

def all_left_right_truncatable_prime(values):
    x = values[37]
    truncatable_primes = []

    def is_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[:i])) or not isprime(int(str(n)[i:])):
                return False
        return True
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)