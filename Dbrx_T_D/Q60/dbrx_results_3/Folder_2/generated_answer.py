from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        while n > 10:
            n = int(str(n)[1:] if n % 10 != 0 else str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = tup[618]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    return [p for p in primes if is_left_right_truncatable(p)]