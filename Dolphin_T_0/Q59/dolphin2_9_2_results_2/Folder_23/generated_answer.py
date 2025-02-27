from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[77]
    primes = [i for i in range(2, x) if isprime(i)]
    primes.sort(reverse=True)
    truncable_primes = []
    for prime in primes:
        if str(prime).count('0') == 0:
            number = prime
            while number:
                if not isprime(number):
                    break
                number = int(str(number)[1:])
            if not number:
                truncable_primes.append(prime)
    return truncable_primes