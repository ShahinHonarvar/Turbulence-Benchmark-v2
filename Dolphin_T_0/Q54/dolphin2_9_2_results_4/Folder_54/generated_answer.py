from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[88]
    primes = []
    for n in range(x - 1, 1, -1):
        if isprime(n):
            trunc = n
            while trunc > 1:
                trunc //= 10
                if not isprime(trunc):
                    break
            else:
                primes.append(n)
    primes.sort(reverse=True)
    return primes