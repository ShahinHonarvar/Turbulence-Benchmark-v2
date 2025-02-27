from sympy import isprime

def all_left_truncatable_prime(tuple_of_integers):

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = tuple_of_integers[91]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])