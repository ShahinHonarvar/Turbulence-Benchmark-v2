from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[32]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    truncatable_primes = []
    for prime in primes:
        digits = len(str(prime))
        for i in range(1, digits + 1):
            if i == 1 and prime in truncatable_primes:
                break
            left_truncate = int(str(prime)[i:])
            right_truncate = int(str(prime)[:-i])
            if not isprime(left_truncate) or not isprime(right_truncate):
                break
            if i == digits:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)