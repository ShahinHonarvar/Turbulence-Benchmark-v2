from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[64]
    left_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if '0' in str(num):
            continue
        if all((isprime(int(str(num)[i:])) for i in range(len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)