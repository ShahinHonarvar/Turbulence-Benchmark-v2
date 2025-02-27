from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[55]
    primes = []
    for number in range(10, x):
        if isprime(number) and all((isprime(int(str(number)[i:-1])) for i in range(1, len(str(number))))):
            primes.append(number)
    return sorted(primes, reverse=True) if primes else []