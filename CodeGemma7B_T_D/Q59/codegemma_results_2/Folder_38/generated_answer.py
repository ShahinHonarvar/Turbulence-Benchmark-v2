from sympy import isprime

def all_left_truncatable_prime(args):
    x = args[28]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n)) - 1):
            if not isprime(int(str(n)[i + 1:])):
                return False
        return True
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)