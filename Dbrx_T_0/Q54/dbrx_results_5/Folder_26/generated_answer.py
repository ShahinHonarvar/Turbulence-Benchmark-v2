from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[81]
    primes = []
    for i in range(10, x):
        if isprime(i):
            is_right_truncatable = True
            while i > 1:
                if not isprime(i):
                    is_right_truncatable = False
                    break
                i = i // 10
            if is_right_truncatable:
                primes.append(i)
    primes.sort(reverse=True)
    return primes