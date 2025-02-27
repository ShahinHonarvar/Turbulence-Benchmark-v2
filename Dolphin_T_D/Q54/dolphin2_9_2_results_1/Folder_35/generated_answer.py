import sympy

def all_right_truncatable_prime(t):
    x = t[177]
    primes = []
    for i in range(2, x):
        if sympy.isprime(i):
            if all(sympy.isprime((int(str(i)[:-j]) for j in range(1, len(str(i)))))):
                primes.append(i)
    return sorted(primes)