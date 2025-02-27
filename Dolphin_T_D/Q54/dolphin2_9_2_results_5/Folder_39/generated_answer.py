from sympy import isprime

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[30]
    primes = []
    for number in range(2, x):
        if isprime(number):
            trunc = number
            while trunc > 1:
                if not isprime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(number)
    return sorted(primes, reverse=True) if primes else []