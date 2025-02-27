from sympy import isprime

def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[100]
    left_truncatable_primes = []
    for n in range(2, x):
        if isprime(n) and '0' not in str(n):
            left_trunc = n
            while left_trunc != 0:
                if not isprime(left_trunc):
                    break
                left_trunc //= 10
            else:
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)