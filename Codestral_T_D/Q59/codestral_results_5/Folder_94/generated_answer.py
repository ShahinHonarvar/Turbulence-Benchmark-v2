from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[43]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and isprime(i):
            truncated = str(i)
            while len(truncated) > 0:
                truncated = truncated[1:]
                if not isprime(int(truncated)):
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)