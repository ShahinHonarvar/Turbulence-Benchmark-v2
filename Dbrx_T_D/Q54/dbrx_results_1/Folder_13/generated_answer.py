from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[784]
    primes = []
    for i in range(10, x):
        if isprime(i):
            is_right_truncatable = True
            while i >= 10:
                i = int(str(i)[:-1])
                if not isprime(i):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                primes.append(i)
    return sorted(primes)