from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[22]
    primes = []
    for num in range(2, x):
        if isprime(num):
            trunc = num
            while trunc > 0:
                if not isprime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    primes.append(num)
    return sorted(primes, reverse=True)