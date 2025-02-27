import sympy

def all_left_truncatable_prime(t):
    x = t[29]
    prime_numbers = [i for i in sympy.primerange(x) if i < x]
    left_truncatable_primes = []
    for prime in prime_numbers:
        if str(prime).startswith('0'):
            continue
        while len(str(prime)) != 0:
            if not sympy.isprime(int(str(prime))):
                break
            else:
                prime = int(str(prime)[1:])
        else:
            left_truncatable_primes.append(int(str(prime)))
    return sorted(left_truncatable_primes, reverse=True)