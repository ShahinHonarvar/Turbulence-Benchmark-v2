from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[18]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        while s:
            if not isprime(int(s)):
                break
            s = s[1:]
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)