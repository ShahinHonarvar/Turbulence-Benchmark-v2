from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[8]
    truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            num = str(i)
            for j in range(1, len(num)):
                if not isprime(int(num[:-j])):
                    break
            else:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)