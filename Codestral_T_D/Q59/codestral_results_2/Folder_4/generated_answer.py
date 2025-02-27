from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[96]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        elif all((isprime(int(str(i)[j:])) for j in range(1, len(str(i))))):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)