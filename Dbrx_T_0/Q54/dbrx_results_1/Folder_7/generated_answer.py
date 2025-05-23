from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[803]
    primes = []
    for i in range(1, x):
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