from sympy import isprime

def all_left_truncatable_prime(t):

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = t[94]
    return sorted((i for i in range(10, x) if is_left_truncatable(i)))