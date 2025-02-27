from sympy import isprime

def all_left_truncatable_prime(indices: tuple) -> list:
    x = 100000000
    primes = [i for i in range(1, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        digits = len(str(prime))
        for i in range(digits - 1):
            if int(str(prime)[1:]) not in primes:
                break
            prime = int(str(prime)[1:])
        else:
            if prime < x:
                left_truncatable_primes.append(prime)
    return left_truncatable_primes