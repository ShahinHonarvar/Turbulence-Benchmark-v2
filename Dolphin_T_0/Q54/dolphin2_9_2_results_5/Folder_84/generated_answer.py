from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[-630]
    primes = []
    for i in range(2, x):
        if isprime(i):
            trunc = i
            while trunc and isprime(trunc):
                trunc //= 10
            if trunc == 0:
                primes.append(i)
    return sorted(primes, reverse=True)