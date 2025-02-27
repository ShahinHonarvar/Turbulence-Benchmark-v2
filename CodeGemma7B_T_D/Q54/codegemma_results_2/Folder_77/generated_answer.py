from sympy import isprime

def all_right_truncatable_prime(x):
    for i in range(767, x):
        y = str(i)[::-1]
        if isprime(int(y)) and isprime(i):
            primes.append(int(y))
    return sorted(primes, reverse=True)