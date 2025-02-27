from sympy import isprime

def all_left_right_truncatable_prime(n):
    primes = [i for i in range(2, n + 1) if isprime(i)]
    lr_truncatable_primes = []
    for prime in primes:
        digits = len(str(prime))
        prime_str = str(prime)
        for i in range(1, digits):
            if not isprime(int(prime_str[i:])):
                break
            if not isprime(int(prime_str[:i])):
                break
            if i == digits - 1:
                lr_truncatable_primes.append(prime)
    lr_truncatable_primes.sort(reverse=True)
    return lr_truncatable_primes