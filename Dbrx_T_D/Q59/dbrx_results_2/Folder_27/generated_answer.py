from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[79]
    primes = []
    for i in range(1, x):
        if isprime(i):
            is_left_truncatable = True
            for j in str(i):
                if not isprime(int(j)):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)