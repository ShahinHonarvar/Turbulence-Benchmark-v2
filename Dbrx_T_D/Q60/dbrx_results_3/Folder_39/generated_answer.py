from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[30]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    trunc_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        prime_str = str(prime)
        digit_count = len(prime_str)
        for i in range(digit_count - 1):
            if not isprime(int(prime_str[i:])):
                break
            if not isprime(int(prime_str[:digit_count - i])):
                break
        else:
            trunc_primes.append(prime)
    return sorted(trunc_primes, reverse=True)