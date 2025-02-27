import sympy

def all_right_truncatable_prime(x):
    primes = []
    _x = int(x[-1])
    for num in sympy.primerange(2, _x):
        n = num
        while n != 0:
            if n != num:
                primes.append(n)
            n //= 10
    return sorted(list(sympy.set(primes)))