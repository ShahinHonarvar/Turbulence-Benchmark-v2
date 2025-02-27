from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[7]
    primes = []
    for i in range(1, 10):
        if isprime(i) and i < x:
            primes.append(i)
    for i in range(10, x):
        if isprime(i):
            is_right_truncatable = True
            while i > 0:
                if not isprime(i):
                    is_right_truncatable = False
                    break
                i = i // 10
            if is_right_truncatable:
                primes.append(i)
    return sorted(list(set(primes)))