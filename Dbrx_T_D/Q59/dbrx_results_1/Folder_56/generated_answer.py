from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[30]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        for i in range(1, len(s)):
            if not isprime(int(s[i:])):
                break
        else:
            left_truncatable_primes.append(prime)
    return left_truncatable_primes