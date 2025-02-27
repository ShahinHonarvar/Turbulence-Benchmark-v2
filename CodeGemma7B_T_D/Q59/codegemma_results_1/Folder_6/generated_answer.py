from sympy import isprime
                                   from itertools import count, filterfalse

def all_left_truncatable_prime(t):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in count(1):
            if not isprime(n):
                return False
            n = int(str(n)[i:])
    return sorted(filterfalse(isprime, count(t[74])))