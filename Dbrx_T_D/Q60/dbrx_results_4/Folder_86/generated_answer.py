from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[126]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    left_right_truncatable_primes = []
    for prime in primes:
        digits = len(str(prime))
        for i in range(1, digits + 1):
            if not isprime(int(str(prime)[i - 1:])):
                break
            if not isprime(int(str(prime)[:-i])):
                break
        else:
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)