from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[945]
    primes = []
    n = 2
    while n < x:
        if isquo(n, 10) != 0 and n % 5 != 0:
            m = n
            while m > 1:
                m //= 10
                if not isprime(m):
                    break
            else:
                primes.append(n)
        n += 1
    return sorted(primes, reverse=True)