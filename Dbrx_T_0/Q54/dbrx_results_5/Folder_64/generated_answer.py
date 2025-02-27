from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[4]
    primes = []
    for i in range(1, x):
        if isprime(i):
            is_right_truncatable = True
            for j in str(i):
                if not isprime(int(j)):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)