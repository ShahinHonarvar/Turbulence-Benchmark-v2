from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[22]
    trunc_primes = []

    def is_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    for n in range(x, 0, -1):
        if isprime(n) and n != 0 and is_truncatable_prime(n):
            trunc_primes.append(n)
    return trunc_primes