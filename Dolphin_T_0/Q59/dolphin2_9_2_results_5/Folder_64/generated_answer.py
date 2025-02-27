from sympy import isprime

def all_left_truncable_prime(t):
    x = t[4]
    primes = []
    for num in range(1, x):
        if isprime(num):
            n = num
            while n != 0:
                if not isprime(n):
                    break
                n //= 10
            else:
                primes.append(num)
    primes.sort()
    return primes