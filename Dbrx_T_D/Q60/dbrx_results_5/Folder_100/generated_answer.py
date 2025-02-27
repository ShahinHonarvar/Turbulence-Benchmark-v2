from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_truncatable_prime(i):
        while i > 0:
            if not isprime(i):
                return False
            i = int(str(i)[1:])
        return True

    def is_right_truncatable_prime(i):
        while i > 0:
            if not isprime(i):
                return False
            i = int(str(i)[:-1])
        return True
    primes = [i for i in range(2, n + 1) if isprime(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p)]
    result = list(set(left_truncatable_primes) & set(right_truncatable_primes))
    result.sort()
    return result