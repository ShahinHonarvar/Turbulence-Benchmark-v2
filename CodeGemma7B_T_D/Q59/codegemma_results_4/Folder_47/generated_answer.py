from sympy import isprime

def all_left_truncatable_prime(arg):
    x = arg[49]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        if not str(prime).startswith('0'):
            truncatable = True
            prime_str = str(prime)
            for i in range(2, len(prime_str)):
                if not isprime(int(prime_str[i:])):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)