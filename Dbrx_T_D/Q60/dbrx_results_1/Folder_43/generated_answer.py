from sympy import isprime

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if isprime(i)]
    ltr_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        x = prime
        while x > 0:
            if not isprime(x):
                break
            x //= 10
        else:
            ltr_primes.append(prime)
    return sorted(list(set(ltr_primes)), reverse=True)