from sympy import isprime

def all_right_truncatable_prime(n):
    x = n[630]
    primes = []
    for i in range(1, x):
        if isprime(i):
            s = str(i)
            while len(s) > 1:
                s = s[:-1]
                if not isprime(int(s)):
                    break
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes