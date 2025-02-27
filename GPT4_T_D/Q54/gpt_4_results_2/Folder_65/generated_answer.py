from sympy import isprime

def all_right_truncatable_prime(tup):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = tup[32]
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])