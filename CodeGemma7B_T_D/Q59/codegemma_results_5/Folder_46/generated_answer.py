from sympy import isprime

def all_left_truncatable_prime(x):
    primes = [i for i in range(x) if isprime(i) and (not str(i).endswith('0'))]
    result = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not isprime(int(str_prime[i:])):
                break
        else:
            result.append(prime)
    return sorted(result)